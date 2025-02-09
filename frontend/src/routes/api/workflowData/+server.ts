import { json } from '@sveltejs/kit';
import { Client, Connection } from '@temporalio/client';
type List = ChatType[];
type ChatType = {
	id: string;
	name: string;
	type: string;
	chat: List;
};

type Chats = {
	chatScreen1: List;
	chatScreen2: List;
	chatScreen3: List;
};
import data from '$lib/data.json';

const role_screen_mapping = data["role_screen_mapping"]

export async function POST({ request }) {
	const { activeChatItems } = await request.json();
	let connectionOptions = {};
	connectionOptions = {
		address: 'localhost:7233'
	};
	const connection = await Connection.connect(connectionOptions);
	const client = new Client({ connection });

	const response: Chats = {
		chatScreen1: [] as List,
		chatScreen2: [] as List,
		chatScreen3: [] as List
	};

	for (const wf of activeChatItems) {
		const handle = client.workflow.getHandle(wf.type + '-' + wf.name + '-' + wf.id);
		// console.log('handle', wf.type + '-' + wf.name + '-' + wf.id);
		const resp: string = await handle.query('get_state');

		const data = JSON.parse(resp);
		const parsed_data = [];
		data.messages.map((block) => {
			if (block.role === 'user') {
                if (Array.isArray(block.content)) {
                    // dum = block.content[0]
                    console.log("");
                }else{
                    // let dum = JSON.parse(block.content);
                    block.content = JSON.parse(block.content);
                    parsed_data.push(block);
                }
                
			} else {
				parsed_data.push(block);
			}
		});
		const chat: ChatType = {
			id: wf.id,
			name: wf.name,
			type: wf.type,
			chat: parsed_data
		};

		const screen = role_screen_mapping[chat.type as keyof typeof role_screen_mapping];
		if (screen) {
			response[screen as keyof Chats].push(chat);
		}
	}

	await client.connection.close();
	return json(response);
}
