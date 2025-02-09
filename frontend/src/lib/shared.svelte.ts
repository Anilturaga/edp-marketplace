interface ChatIndexType {
	id: string;
	name: string;
	type: string;
}

interface ChatType {
	role: string;
	content: string | string[] | object;
}


export interface MultiChatMap {
	id: string;
	name: string;
	type: string;
	chat: ChatType[];
}

interface HeaderState {
	toggle: boolean;
	chatIndex: ChatIndexType[];
	activeChat: string;
	chatScreen1: MultiChatMap[];
	chatScreen2: MultiChatMap[];
	chatScreen3: MultiChatMap[];
}

export const headerState = $state<HeaderState>({
	toggle: true,
	chatIndex: [
		// {
		// 	id: 'default',
		// 	name: `New Chat`
		// },
		
	],
	activeChat: "default",
	chatScreen1: [
		// {
		// 	name: 'Anil',
		// 	chat: []
		// }
	],
	chatScreen2: [
		// {
		// 	name: 'Offer Agent 1',
		// 	chat: []
		// },
		// {
		// 	name: 'Offer Agent 2',
		// 	chat: []
		// },
		// {
		// 	name: 'Offer Agent 3',
		// 	chat: []
		// }
	],
	chatScreen3: [
		// {
		// 	id: 'default',
		// 	name: 'Merchant 1',
		// 	chat: []
		// }
	]
});
