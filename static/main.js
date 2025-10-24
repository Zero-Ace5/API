const taskList = document.getElementById('taskList');
const taskInput = document.getElementById('taskInput');
const addBtn = document.getElementById('addBtn');

async function loadTasks() {
    const res = await fetch('/api/tasks');
    const data = await res.json();
    taskList.innerHTML = '';
    data.forEach(t => {
        const li = document.createElement('li');
        li.textContent = t.title;
        li.onclick = () => deleteTask(t.id);
        taskList.appendChild(li);
    });
}

async function addTask() {
    const title = taskInput.value.trim();
    if (!title) return;
    await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title })
    });
    taskInput.value = '';
    loadTasks();
}

async function deleteTask(id) {
    await fetch(`/api/tasks/${id}`, { method: 'DELETE' });
    loadTasks();
}

addBtn.onclick = addTask;
loadTasks();
