async function destSearch() {
    try {
        let id = document.getElementById("img-results-top-track").getAttribute("data-srch-id");
        
        const response = await fetch(`destSearch/${id}`)
        .then(response => response.json())
        .then(destinations => {
            // Print Log for the email data
            console.log(destinations);
            let cnt = 1;
            destinations.response.destinations.forEach(destination => {
                // Update value in div
                try {
                    const cap = document.getElementById("fig" + cnt);
                    cap.innerHTML = destination.destination_name;
                    const figid = document.getElementById("img-result-" + cnt);
                    figid.id = destination.destination_name;
                    cnt++;
                    const destinationName = destination.destination_name + ", " + destination.destination_country;
                    const imagesData = imageSearch(destinationName);
                }
                    
                catch (error) {
                    console.error(error);
                }

            });
        })
    } catch (error) {
        console.error(error);
    }
}

async function imageSearch(destination) {
    try {
        const imageRes = await fetch(`/singleImageSearch/${destination}`);
        const image = await imageRes.json();
        console.log(image.response);

        // Display the image
        const destName = destination.split(", ")[0];
        const pc = document.getElementById(destName);
        pc.src = image.response;
        pc.style.cursor = "pointer";
        pc.addEventListener("click", () => viewDest(destName));
        const pcap = document.getElementById(destName).parentElement.lastElementChild
        pcap.style.cursor = "pointer";
        pcap.addEventListener("click", () => viewDest(destName));
        let sm = document.getElementById("searchMessage");
        sm.style.display = "none";
        let mb = document.getElementById("modifySearch");
        mb.removeAttribute("disabled");
        let mbmb = document.getElementById("modifySearchMobile");
        mbmb.removeAttribute("disabled");
        let vm = document.getElementById("viewMore");
        vm.removeAttribute("disabled");
        let vmmb = document.getElementById("viewMoreMobile");
        vmmb.removeAttribute("disabled");
    } catch (error) {
        console.error(error);
    }
}

async function viewMoreDestSearch() {
    const hideShow = document.querySelectorAll(".hideShow");
    hideShow.forEach(item => {item.style.display = "block";});
    viewMore.setAttribute("disabled","true");
    viewMoreMobile.setAttribute("disabled","true");
    let mb = document.getElementById("modifySearch");
    mb.setAttribute("disabled","true");
    let mbmb = document.getElementById("modifySearchMobile");
    mbmb.setAttribute("disabled","true");
    let sm = document.getElementById("searchMessage");
    sm.style.display = "block";
    try {
        let id = document.getElementById("img-results-more-track").getAttribute("data-srch-id");
        const response = await fetch(`destSearch/${id}`)
        .then(response => response.json())
        .then(destinations => {
            // Print Log for the email data
            console.log(destinations);
            let cnt = 1;
            destinations.response.destinations.forEach(destination => {
                // Update value in div
                try {
                    const cap1 = document.getElementById("figMore" + cnt);
                    cap1.innerHTML = destination.destination_name;
                    const figid1 = document.getElementById("img-result-more-" + cnt);
                    figid1.id = destination.destination_name;
                    cnt++;
                    const destinationName1 = destination.destination_name + ", " + destination.destination_country;
                    const imagesData1 = viewMoreImageSearch(destinationName1);
                }
                catch (error) {
                    console.error(error);
                }
            });
        })
    } catch (error) {
        console.error(error);
    }
}

async function viewMoreImageSearch(destination) {
    try {
        const imageRes1 = await fetch(`/singleImageSearch/${destination}`);
        const image1 = await imageRes1.json();
        console.log(image1.response);

        // Display the image
        const destName1 = destination.split(", ")[0];
        const pc1 = document.getElementById(destName1);
        pc1.src = image1.response;
        pc1.style.cursor = "pointer";
        pc1.addEventListener("click", () => viewDest(destName1));
        const pcap1 = document.getElementById(destName1).parentElement.lastElementChild
        pcap1.style.cursor = "pointer";
        pcap1.addEventListener("click", () => viewDest(destName1));
        let sm1 = document.getElementById("searchMessage");
        sm1.style.display = "none";
        let mb = document.getElementById("modifySearch");
        mb.removeAttribute("disabled");
        let mbmb = document.getElementById("modifySearchMobile");
        mbmb.removeAttribute("disabled");
    } catch (error) {
        console.error(error);
    }
}

function viewDest(destination_name) {
    window.location.href = `/destView/${destination_name}`;
}

// Call destSearch when the DOM is loaded
document.addEventListener('DOMContentLoaded', destSearch);

// View more button tracking
const viewMore = document.getElementById("viewMore");
viewMore.addEventListener("click", viewMoreDestSearch);
const viewMoreMobile = document.getElementById("viewMoreMobile");
viewMoreMobile.addEventListener("click", viewMoreDestSearch);