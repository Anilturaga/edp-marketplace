<script lang="ts">
	import { headerState } from '$lib/shared.svelte.js';
	import Builder from '$lib/Builder.svelte';
	import ChatGroup from '$lib/ChatGroup.svelte';
	import { fetchData } from '$lib/apicalls.svelte.js';

	$effect(() => {
		const id = setInterval(async () => {
			const issuerIds: string[] = ['Offer Agent 1', 'Offer Agent 2', 'Offer Agent 3'];
			const merchantIds: string[] = ['Merchant 1', 'Merchant 2', 'Merchant 3'];
			// dummy data
			headerState.customerChat = [
				{
					name: 'Anil',
					chat: []
				}
			];
			headerState.issuerChat = [
				{
					name: 'Offer Agent 1',
					chat: []
				},
				{
					name: 'Offer Agent 2',
					chat: []
				},
				{
					name: 'Offer Agent 3',
					chat: []
				}
			];
			headerState.merchantChat = [];
		}, 1000);
		return () => {
			clearInterval(id);
		};
	});
</script>

{#if headerState.toggle === true}
	<Builder />
{:else}
	<ChatGroup />
{/if}
