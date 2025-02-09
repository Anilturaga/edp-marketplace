<script lang="ts">
	import { headerState } from '$lib/shared.svelte.js';
	import Builder from '$lib/Builder.svelte';
	import ChatGroup from '$lib/ChatGroup.svelte';
</script>

{#if headerState.toggle === true}
	<Builder />
{:else}
	<ChatGroup />
{/if}
