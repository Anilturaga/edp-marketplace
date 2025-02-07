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
</script>

<div class="flex flex-row w-full h-[93%] py-2 gap-2">
	{#each [headerState.customerChat, headerState.issuerChat, headerState.merchantChat] as chats, columnIndex}
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
								class="bg-base-200 p-3 cursor-pointer select-none flex justify-between items-center"
								onclick={() => toggle(columnIndex, i)}
							>
								{chat.name}
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
