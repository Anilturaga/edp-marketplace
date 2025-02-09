<script lang="ts">
	import { headerState } from '$lib/shared.svelte.js';
	import { ChevronDown, ChevronUp } from 'lucide-svelte';
	import { fade } from 'svelte/transition';
	import Chat from '$lib/Chat.svelte';

	let openIndexes = $state([0, 0, 0]);

	function toggle(columnIndex: number, itemIndex: number) {
		openIndexes[columnIndex] = openIndexes[columnIndex] === itemIndex ? -1 : itemIndex;
		openIndexes = openIndexes;
	}

	$effect(() => {
		if (headerState.activeChat === 'default') return;
		const id = setInterval(async () => {
			const activeChatItems = headerState.chatIndex.filter(item => item.id === headerState.activeChat);
			const response = await fetch('/api/workflowData', {
				method: 'POST',
				body: JSON.stringify({ activeChatItems }),
				headers: {
					'Content-Type': 'application/json'
				}
			});
			const data = await response.json();
			// console.log(data);

			headerState.chatScreen1 = data.chatScreen1;
			headerState.chatScreen2 = data.chatScreen2;
			headerState.chatScreen3 = data.chatScreen3;
		}, 2000);
		return () => {
			clearInterval(id);
		};
	});
	const colors = [
	"primary",
	"secondary",
	"accent",
	]
</script>

<div class="flex flex-row w-full h-[93%] py-2 gap-2">
	{#each [headerState.chatScreen1, headerState.chatScreen2, headerState.chatScreen3] as chats, columnIndex}
		<div class="h-full w-1/3 rounded-lg flex flex-col">
			{#if chats.length === 0}
				<div class="flex items-center justify-center h-full flex-col bg-base-200 rounded-lg my-1">
					<div class="loading loading-ring loading-lg"></div>
					<div class="btn btn-ghost">Polling for agents...</div>
				</div>
			{:else}
				<div class="flex flex-col h-full">
					{#each chats as chat, i}
						<div
							class={`flex flex-col overflow-hidden  ${openIndexes[columnIndex] === i ? 'flex-1' : 'flex-none'} my-1 rounded-lg`}
						>
							<button
								class="bg-base-200 p-3 cursor-pointer select-none flex justify-between items-center font-bold"
								onclick={() => toggle(columnIndex, i)}
							>
							    <div>
								{chat.name}
								<span class={`badge badge-sm badge-${colors[columnIndex]}`}>{chat.type.toLocaleUpperCase()}</span>
							    </div>
								{#if openIndexes[columnIndex] === i}
									<ChevronUp class="w-5 h-5" />
								{:else}
									<ChevronDown class="w-5 h-5" />
								{/if}
							</button>
							{#if openIndexes[columnIndex] === i}
								<div class="bg-base-100 p-3 overflow-y-auto flex-1" in:fade>
									<Chat {chat} />
								</div>
							{/if}
						</div>
					{/each}
				</div>
			{/if}
		</div>
	{/each}
</div>
