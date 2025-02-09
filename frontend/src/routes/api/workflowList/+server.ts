import { json } from '@sveltejs/kit';
import { Client, Connection } from '@temporalio/client';

type ChatIndexItem = {
	id: string;
	name: string;
	type: string;
};

export async function POST() {
	try {
		let connectionOptions = {};
		connectionOptions = {
			address: 'localhost:7233'
		};
		const connection = await Connection.connect(connectionOptions);
		const client = new Client({ connection });
		// const client = new Client();
		const wf = await client.workflowService.listOpenWorkflowExecutions({ namespace: 'default' });
		// console.log('execs', wf);

		const chatIndex: ChatIndexItem[] = [];
		wf.executions.forEach((exec) => {
			// console.log('exec', exec.execution?.workflowId, '\n\n');
			chatIndex.push({
				id: exec.execution?.workflowId?.split('-')[2] ?? '',
				name: exec.execution?.workflowId?.split('-')[1] ?? '',
				type: exec.execution?.workflowId?.split('-')[0] ?? ''
			});
		});
		await client.connection.close();
		return json(chatIndex);
	} catch (error) {
		console.error('Error fetching workflow executions:', error);
		return json([]);
	}
}
