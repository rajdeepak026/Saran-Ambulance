document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('partnerCarousel');

  const partners = [
    {
      name: "City Hospital",
      location: "Chapra, Saran",
      image: "https://via.placeholder.com/100x100.png?text=City+Hospital",
      link: "https://cityhospital.example.com"
    },
    {
      name: "LifeCare Clinic",
      location: "Marhaura Road",
      image: "https://via.placeholder.com/100x100.png?text=LifeCare",
      link: "https://lifecareclinic.example.com"
    },
    {
      name: "Saran Health NGO",
      location: "Ekma, Bihar",
      image: "https://via.placeholder.com/100x100.png?text=Saran+NGO",
      link: "https://saranhealth.ngo"
    },
    {
      name: "Universal Medical",
      location: "Baniyapur",
      image: "https://via.placeholder.com/100x100.png?text=Universal",
      link: "https://universalmed.example.com"
    },
    {
      name: "Rescue Alliance",
      location: "Manjhi",
      image: "https://via.placeholder.com/100x100.png?text=Rescue",
      link: "https://rescuealliance.org"
    },
    {
      name: "Doctor's Point",
      location: "Siwan",
      image: "https://via.placeholder.com/100x100.png?text=Doctors+Point",
      link: "https://doctorspoint.example.com"
    },
    {
      name: "Star Hospital",
      location: "Garkha",
      image: "https://via.placeholder.com/100x100.png?text=Star+Hospital",
      link: "#"
    },
    {
      name: "Apollo First Aid",
      location: "Maker",
      image: "https://via.placeholder.com/100x100.png?text=Apollo",
      link: "#"
    },
    {
      name: "Green Cross",
      location: "Amnour",
      image: "https://via.placeholder.com/100x100.png?text=Green+Cross",
      link: "#"
    },
    {
      name: "Safe Hands",
      location: "Darihara",
      image: "https://via.placeholder.com/100x100.png?text=Safe+Hands",
      link: "#"
    }
  ];

  // Load partner cards
  partners.forEach(partner => {
    const card = document.createElement('div');
    card.className = 'card me-3 shadow-sm text-center';
    card.style.minWidth = '250px';
    card.innerHTML = `
      <div class="pt-3">
        <a href="${partner.link}" target="_blank" title="${partner.name}">
          <img src="${partner.image}" alt="${partner.name}" class="rounded-circle" style="width: 100px; height: 100px; object-fit: cover;">
        </a>
      </div>
      <div class="card-body">
        <h5 class="card-title mb-1">
          <a href="${partner.link}" target="_blank" class="text-decoration-none text-dark">${partner.name}</a>
        </h5>
        <p class="card-text text-muted" style="font-size: 0.9rem;">${partner.location}</p>
      </div>
    `;
    container.appendChild(card);
  });

  // Auto-scroll logic
  let scrollAmount = 0;
  const scrollStep = 1;
  const scrollDelay = 20;

  function autoScroll() {
    if (scrollAmount >= container.scrollWidth - container.clientWidth) {
      scrollAmount = 0;
      container.scrollLeft = 0;
    } else {
      scrollAmount += scrollStep;
      container.scrollLeft += scrollStep;
    }
  }

  setInterval(autoScroll, scrollDelay);
});
