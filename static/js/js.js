const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
    const li = item.parentElement;

    item.addEventListener('click', function () {
        allSideMenu.forEach(i=> {
            i.parentElement.classList.remove('active');
        })
        li.classList.add('active');
    })
});




// TOGGLE SIDEBAR
const sidebar = document.getElementById("sidebar");
const menuIcon = document.querySelector(".bx-menu");

menuIcon.addEventListener("click", () => {
  sidebar.classList.toggle("active");
});








const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
    if(window.innerWidth < 576) {
        e.preventDefault();
        searchForm.classList.toggle('show');
        if(searchForm.classList.contains('show')) {
            searchButtonIcon.classList.replace('bx-search', 'bx-x');
        } else {
            searchButtonIcon.classList.replace('bx-x', 'bx-search');
        }
    }
})





if(window.innerWidth < 768) {
    sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
    searchButtonIcon.classList.replace('bx-x', 'bx-search');
    searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
    if(this.innerWidth > 576) {
        searchButtonIcon.classList.replace('bx-x', 'bx-search');
        searchForm.classList.remove('show');
    }
})



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
    if(this.checked) {
        document.body.classList.add('dark');
    } else {
        document.body.classList.remove('dark');
    }
})

// Get the "add" button and the to-do list
const addBtn = document.getElementById("addBtn");
const todoList = document.getElementById("todoList");

// Add event listener to the "add" button
addBtn.addEventListener("click", () => {
  // Create a new to-do item and add it to the list
  const newTodo = document.createElement("li");
  newTodo.innerHTML = `
    <p contenteditable="true">New Todo</p>
    <i class='bx bx-dots-vertical-rounded'></i>
  `;
  todoList.appendChild(newTodo);
});

// Add event listener to the to-do list
todoList.addEventListener("click", (event) => {
  const target = event.target;
  if (target.tagName === "LI") {
    // Toggle the "completed" class on the clicked item
    target.classList.toggle("completed");
  } else if (target.classList.contains("bx-dots-vertical-rounded")) {
    // Show a context menu with "Edit" and "Delete" options
    const contextMenu = document.createElement("div");
    contextMenu.innerHTML = `
      <ul>
        <li>Edit</li>
        <li>Delete</li>
      </ul>
    `;
    contextMenu.style.position = "absolute";
    contextMenu.style.top = `${event.clientY}px`;
    contextMenu.style.left = `${event.clientX}px`;
    todoList.appendChild(contextMenu);

    // Add event listener to the context menu
    contextMenu.addEventListener("click", (event) => {
      if (event.target.textContent === "Edit") {
        // Enable content editing on the clicked item
        const todoText = target.querySelector("p");
        todoText.contentEditable = true;
        todoText.focus();
      } else if (event.target.textContent === "Delete") {
        // Remove the clicked item from the list
        target.remove();
      }

      // Remove the context menu from the DOM
      contextMenu.remove();
    });
  }
});
