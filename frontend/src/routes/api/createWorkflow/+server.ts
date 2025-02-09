import { json } from '@sveltejs/kit';
import { Client, Connection } from '@temporalio/client';

export async function POST({request}) {
	try {
    	const { workflowId, taskQueue, args } = await request.json();

		let connectionOptions = {};
		connectionOptions = {
			address: 'localhost:7233'
		};
		const connection = await Connection.connect(connectionOptions);
		const client = new Client({ connection });
		// const client = new Client();
		console.log(workflowId, taskQueue, args)
		const handle = await client.workflow.start('Workflow', {
			workflowId: workflowId,
			taskQueue: taskQueue,
			args: args // this is typechecked against workflowFn's args
		});
		// const handle = client.getHandle(workflowId);
		// const wf = await client.workflowService.listOpenWorkflowExecutions({ namespace: 'default' });
		// // console.log('execs', wf);

		// const chatIndex: ChatIndexItem[] = [];
		// wf.executions.forEach((exec) => {
		// 	// console.log('exec', exec.execution?.workflowId, '\n\n');
		// 	chatIndex.push({
		// 		id: exec.execution?.workflowId?.split('-')[2] ?? '',
		// 		name: exec.execution?.workflowId?.split('-')[1] ?? '',
		// 		type: exec.execution?.workflowId?.split('-')[0] ?? ''
		// 	});
		// });
		await client.connection.close();
		return json({status: 'success', workflowId: workflowId});
	} catch (error) {
		console.error('Error fetching workflow executions:', error);
		return json({status: 'error', error: error});
	}
}
