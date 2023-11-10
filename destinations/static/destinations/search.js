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
    } catch (error) {
        console.error(error);
    }
}

function viewDest(destination_name) {
    window.location.href = `/destView/${destination_name}`;
}

// Call destSearch when the DOM is loaded
document.addEventListener('DOMContentLoaded', destSearch);