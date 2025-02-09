<script lang="ts">
	import { headerState } from '$lib/shared.svelte.js';
	import { ChevronDown, ChevronUp, MessageSquare } from 'lucide-svelte';
	import { fade } from 'svelte/transition';
	import Chat from '$lib/Chat.svelte';
	import data from '$lib/data.json';

	let greeting: string;

	function getGreeting() {
		const hours = new Date().getHours();
		if (hours < 12) {
			return 'Good morning';
		} else if (hours < 18) {
			return 'Good afternoon';
		} else {
			return 'Good evening';
		}
	}

	greeting = getGreeting();

	const riskProfileClasses = {
		Good: 'success',
		Medium: 'warning',
		Poor: 'error'
	};

	const userProfileBadges = {
		Premium: 'badge-secondary',
		Standard: 'badge-primary'
	};

	function generateRandomString(length: number) {
		const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
		let result = '';
		for (let i = 0; i < length; i++) {
			result += chars.charAt(Math.floor(Math.random() * chars.length));
		}
		return result;
	}

	async function handleClick(persona: any) {
		const runId = generateRandomString(4);
		const workflowId = `${persona.type}-${persona.User}-${runId}`;
		const taskQueue = `${persona.User}-queue`;
		const args = [{
			user_id: persona.User,
			run_id: runId
		}];
		// const args = [persona.User, runId];

		try {
			const response = await fetch('/api/createWorkflow', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					workflowId,
					taskQueue,
					args
				})
			});
			headerState.activeChat = runId;
			headerState.toggle = false;

			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
		} catch (error) {
			console.error('Error:', error);
		}
	}
</script>

<div class="flex flex-col justify-center items-center w-full h-[93%] py-2">
	<h1 class="text-3xl font-bold mb-2">👋 {greeting}</h1>
	<h2 class="text-lg text-base-content/70 mb-8">Start a chat from any of the consumer personas.</h2>
	<div class="flex flex-row justify-center items-center gap-8 w-full px-8">
		{#each data.personas as persona}
			<div
				class="h-full w-1/3 rounded-lg flex flex-col p-4 bg-base-200 cursor-pointer hover:shadow-lg transition-all duration-200 hover:-translate-y-1"
			>
				<h2 class="text-xl font-bold mb-2">{persona.User}</h2>

				<div class="flex flex-col gap-2">
					<div class="stats bg-base-100 shadow">
						<div class="stat">
							<div class="stat-title">Credit Score</div>
							<div class="stat-value text-{riskProfileClasses[persona.risk_profile]}">
								{persona.credit_score}
							</div>
						</div>
					</div>

					<div class="flex justify-between items-center">
						<span class="text-base-content">Risk Profile:</span>
						<span class="badge badge-{riskProfileClasses[persona.risk_profile]}"
							>{persona.risk_profile}</span
						>
					</div>

					<div class="flex justify-between items-center">
						<span class="text-base-content">User Profile:</span>
						<span class="badge {userProfileBadges[persona.user_profile]}"
							>{persona.user_profile}</span
						>
					</div>

					<div class="stats bg-base-100 shadow">
						<div class="stat">
							<div class="stat-title">Points Available</div>
							<div class="stat-value text-primary">{persona.points_redeemable}</div>
							<progress
								class="progress progress-primary w-full"
								value={persona.points_redeemable / 100}
								max="100"
							></progress>
						</div>
					</div>
				</div>

				<button class="btn btn-primary mt-4" onclick={() => handleClick(persona)}>
					<MessageSquare class="w-4 h-4 mr-2" />
					Start Chat
				</button>
			</div>
		{/each}
	</div>
</div>
