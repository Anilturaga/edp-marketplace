<script>
	import { LucideCirclePlus, LucideMessagesSquare } from 'lucide-svelte';
	import { headerState } from '$lib/shared.svelte.js';
	$effect(() => {
		const id = setInterval(async () => {
			const response = await fetch('/api/workflowList', {
				method: 'POST',
				// body: JSON.stringify({ description }),
				headers: {
					'Content-Type': 'application/json'
				}
			});
			const data = await response.json();
			headerState.chatIndex = data;
		}, 1000);
		return () => {
			clearInterval(id);
		};
	});
</script>

<div class="navbar bg-base-200 rounded-xl px-6">
	<div class="w-1/4 flex justify-start text-xl font-bold">Visa Nova</div>
	<div class="w-1/2">
		<select
			class="select select-md select-bordered w-full flex justify-center text-center"
			bind:value={headerState.activeChat}
			onchange={() => {
                if (headerState.activeChat === "default") return;
                headerState.toggle = false;
            }}
		>
		<option disabled selected value="default">Chat Threads</option>
			{#each headerState.chatIndex as chatIndex, i}
				{#if chatIndex.type === 'consumer'}
					<option value={chatIndex.id}>
						{chatIndex.name} - {chatIndex.id}
					</option>
				{/if}
			{/each}
		</select>
	</div>
	<div class="w-1/4 flex justify-end">
		<label class="swap swap-rotate">
			<!-- this hidden checkbox controls the state -->
			<input 
				type="checkbox" 
				bind:checked={headerState.toggle}
			/>
			<LucideCirclePlus class="swap-off" size={27} />
			<LucideMessagesSquare class="swap-on" size={27} />
		</label>
	</div>
</div>
