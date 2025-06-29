document.addEventListener("DOMContentLoaded", () => {
  const blogs = [
    {
      title: "Top 10 Emergency Tips Everyone Should Know",
      image: "https://source.unsplash.com/600x400/?healthcare",
      date: "June 15, 2025",
      desc: "Learn crucial first-aid and emergency response tips to stay prepared in critical situations.",
      link: "blog-top-10-emergency-tips.html" // <-- Your blog page
    },
    {
      title: "How Saran Ambulance Reaches You in Under 10 Minutes",
      image: "https://source.unsplash.com/600x400/?ambulance",
      date: "June 10, 2025",
      desc: "Explore our rapid response system and how technology helps us serve you faster.",
      link: "#"
    },
    {
      title: "Understanding ICU Ambulances: When You Need One",
      image: "https://source.unsplash.com/600x400/?doctor",
      date: "June 1, 2025",
      desc: "A deep dive into what makes ICU ambulances life-saving for critical patients.",
      link: "#"
    }
  ];

  const blogContainer = document.getElementById("blogCards");

  blogs.forEach((blog) => {
    const col = document.createElement("div");
    col.className = "col-md-4";

    col.innerHTML = `
      <div class="card h-100 shadow-sm border-0">
        <img src="${blog.image}" class="card-img-top" alt="${blog.title}">
        <div class="card-body">
          <h5 class="card-title">${blog.title}</h5>
          <p class="card-text text-muted small">${blog.date}</p>
          <p class="card-text">${blog.desc}</p>
        </div>
        <div class="card-footer bg-transparent border-0">
          <a href="${blog.link}" class="btn btn-outline-primary btn-sm">Read More</a>
        </div>
      </div>
    `;

    blogContainer.appendChild(col);
  });
});
