const body = document.querySelector("body"),
	sidebar = body.querySelector(".sidebar"),
	toggle = body.querySelector(".toggle"),
	searchBtn = body.querySelector(".search-box");

const closesidebar = () => {
	sidebar.classList.toggle("away");
};

toggle.addEventListener("click", closesidebar);


