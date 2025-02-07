<script>
	import { LucideHammer, LucideMessagesSquare } from 'lucide-svelte';
	import { headerState } from '$lib/shared.svelte.js';
</script>

<div class="navbar bg-base-200 rounded-xl px-6">
	<div class="w-1/4 flex justify-start text-xl font-bold">Visa Nova</div>
	<div class="w-1/2">
		<select
			class="select select-md select-bordered w-full flex justify-center text-center"
			bind:value={headerState.activeChat}
		>
			{#each headerState.chatIndex as chatIndex, i}
				<option value={chatIndex.id} selected={chatIndex.id === headerState.chatIndex[i].id}>
					{chatIndex.name}
				</option>
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
			<LucideHammer class="swap-off" size={27} />
			<LucideMessagesSquare class="swap-on" size={27} />
		</label>
	</div>
</div>
