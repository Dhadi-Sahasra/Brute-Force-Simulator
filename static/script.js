async function startSimulation() {

    const password = document.getElementById("password").value;

    if (password === "") {

        alert("Please enter a password.");

        return;

    }

    document.getElementById("status").innerHTML = "Running Simulation...";

    document.getElementById("progress-bar").style.width = "30%";

    const response = await fetch("/simulate", {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify({

            password: password

        })

    });

    const data = await response.json();

    document.getElementById("progress-bar").style.width = "100%";

    document.getElementById("status").innerHTML = "✅ Password Found";

    document.getElementById("foundPassword").innerHTML = data.password;

    document.getElementById("attempts").innerHTML = data.attempts;

    document.getElementById("time").innerHTML = data.time_taken + " seconds";

}