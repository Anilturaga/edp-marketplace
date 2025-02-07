<script>
	import { LucideBot, LucideDownload, LucideUpload, LucideUser } from 'lucide-svelte';
</script>

<div class="h-full flex flex-col">
	<div class="flex-grow overflow-y-auto p-4">
		<div role="alert" class="alert my-2">
			<LucideUser class="stroke-info h-6 w-6 shrink-0" />
			<span>12 unread messages. Tap to see.12 unread messages. Tap to see.12 unread messages.</span>
		</div>
		<div role="alert" class="alert my-2">
			<LucideBot class="stroke-info h-6 w-6 shrink-0" />
			<span>14 unread messages. Tap to see.</span>
		</div>
		<div role="alert" class="alert my-2">
			<LucideUpload class="stroke-info h-6 w-6 shrink-0" />
			<div>
				<h3 class="font-bold">HDFC</h3>
				<div class="text-xs">You have 1 unread message</div>
			</div>
		</div>
		<div role="alert" class="alert my-2">
			<LucideDownload class="stroke-info h-6 w-6 shrink-0" />
			<div>
				<h3 class="font-bold">ICICI</h3>
				<div class="text-xs">Star wars lego set delivered in the next 2 days</div>
			</div>
		</div>
	</div>
	<div class="mx-2 mb-2">
		<div class="join w-full">
			<input
				type="text"
				placeholder="Type a message..."
				class="input input-bordered join-item w-full focus:outline-none"
			/>
			<button class="btn join-item">Send</button>
		</div>
	</div>
</div>
