<script lang="ts">
	import type { MultiChatMap } from '$lib/shared.svelte';
	import { json } from '@sveltejs/kit';
	import { marked } from 'marked';
	import {
		LucideBot,
		LucideDownload,
		LucideUpload,
		LucideUser,
		LucideAlarmClockCheck,
		LucideCalendarClock,
		LucideSend
	} from 'lucide-svelte';
	let { chat }: MultiChatMap = $props();
	console.log(chat);
	let chatInput = $state('');

	async function handleClick() {
		const workflowId = `${chat.type}-${chat.name}-${chat.id}`;
		const taskQueue = `${chat.name}-queue`;

		console.log('send signal', workflowId, taskQueue, chatInput);

		try {
			const response = await fetch('/api/sendUserSignal', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					workflowId,
					taskQueue,
					chatInput
				})
			});
			chatInput = '';

			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
		} catch (error) {
			console.error('Error:', error);
		}
	}
</script>

<div class="h-full flex flex-col">
	<div class="flex-grow overflow-y-auto p-4">
		{#each chat.chat as chatTurn}
			{#if chatTurn.role === 'user'}
				{#if chatTurn.content.from === 'user'}
					<div role="alert" class="alert my-2 flex items-start gap-4">
						<LucideUser class="stroke-info h-6 w-6 shrink-0 mt-1" />
						<div>
							<article class="prose">{@html marked(chatTurn.content.message)}</article>
							<div class="text-xs text-gray-500">{chatTurn.content.current_time}</div>
						</div>
					</div>
				{/if}
				{#if chatTurn.content.from === 'agent'}
					<div role="alert" class="alert my-2 flex items-start gap-4">
						<LucideDownload class="stroke h-6 w-6 shrink-0 mt-1" />
						<div>
							<h3 class="font-bold">{chatTurn.content.agent_id}</h3>
							<article class="prose">{@html marked(chatTurn.content.message)}</article>
							<div class="text-xs text-gray-500">{chatTurn.content.current_time}</div>
						</div>
					</div>
				{/if}
				{#if chatTurn.content.from === 'scheduled_reminder'}
					<div role="alert" class="alert my-2 flex items-start gap-4">
						<LucideAlarmClockCheck class="stroke h-6 w-6 shrink-0 mt-1" />
						<div>
							<h3 class="font-bold">Reminder</h3>
							<article class="prose">{@html marked(chatTurn.content.message)}</article>
							<div class="text-xs text-gray-500">{chatTurn.content.current_time}</div>
						</div>
					</div>
				{/if}
			{/if}
			{#if chatTurn.role === 'assistant'}
				{#each chatTurn.content as tool_use}
					{#if 'agent_messages' in tool_use.input}
						{#each tool_use.input.agent_messages as ag_msg}
							<div role="alert" class="alert my-2 flex items-start gap-4">
								<LucideUpload class="stroke h-6 w-6 shrink-0 mt-1" />
								<div>
									<h3 class="font-bold">{ag_msg.to_id}</h3>
									<article class="prose">{@html marked(ag_msg.message)}</article>
									<div class="text-xs text-gray-500">{chatTurn.content.current_time}</div>
								</div>
							</div>
						{/each}
					{/if}
					{#if 'operator_message' in tool_use.input}
						{#if tool_use.input.operator_message !== '' && tool_use.input.operator_message !== 'null'}
							<div role="alert" class="alert my-2 flex items-start gap-4">
								<LucideBot class="stroke-info h-6 w-6 shrink-0 mt-1" />
								<div>
									<article class="prose">{@html marked(tool_use.input.operator_message)}</article>
								</div>
							</div>
						{/if}
					{/if}
					{#if 'schedule_reminder' in tool_use.input}
						<div role="alert" class="alert my-2 flex items-start gap-4">
							<LucideCalendarClock class="stroke h-6 w-6 shrink-0 mt-1" />
							<div>
								<h3 class="font-bold">In {tool_use.input.schedule_reminder.time} Seconds</h3>
								<article class="prose">
									{@html marked(tool_use.input.schedule_reminder.message)}
								</article>
								<div class="text-xs text-gray-500">{chatTurn.content.current_time}</div>
							</div>
						</div>
					{/if}
				{/each}
			{/if}
		{/each}
	</div>
	<div class="mx-2 mb-2">
		<div class="join w-full">
			<input
				type="text"
				placeholder="Type a message..."
				class="input input-bordered join-item w-full focus:outline-none"
				bind:value={chatInput}
			/>
			<button class="btn join-item" onclick={() => handleClick()}><LucideSend /></button>
		</div>
	</div>
</div>
