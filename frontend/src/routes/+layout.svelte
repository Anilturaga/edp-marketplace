<script lang="ts">
	import '../app.css';
	import Header from '$lib/Header.svelte';
	let { children } = $props();
</script>

<div class="h-screen w-screen p-2">
	<div class="h-[7%] border-0">
		<Header />
	</div>
	{@render children()}
</div>
