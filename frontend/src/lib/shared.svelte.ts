interface ChatIndexType {
	id: string;
	name: string;
}

interface ChatType {
	role: string;
	content: string;
}

interface MultiChatMap {
	name: string;
	chat: ChatType[];
}

interface HeaderState {
	toggle: boolean;
	chatIndex: ChatIndexType[];
	activeChat: string;
	customerChat: MultiChatMap[];
	issuerChat: MultiChatMap[];
	merchantChat: MultiChatMap[];
}

export const headerState = $state<HeaderState>({
	toggle: true,
	chatIndex: [
		// {
		// 	id: 'default',
		// 	name: `New Chat`
		// },
		{
			id: '1',
			name: `Anil`
		},
		{
			id: '2',
			name: `Ayushman`
		},
		{
			id: '3',
			name: `Prahastha`
		}
	],
	activeChat: '1',
	customerChat: [
		// {
		// 	name: 'Anil',
		// 	chat: []
		// }
	],
	issuerChat: [
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
	merchantChat: [
		// {
		// 	id: 'default',
		// 	name: 'Merchant 1',
		// 	chat: []
		// }
	]
});
