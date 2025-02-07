export async function fetchRunningWorkflows() {
  // Simulating network delay
  await new Promise(resolve => setTimeout(resolve, 100));
  return new Date().toLocaleTimeString();
}


export async function fetchData(){
  // Simulating network delay
  await new Promise(resolve => setTimeout(resolve, 100));
  return new Date().toLocaleTimeString();
}