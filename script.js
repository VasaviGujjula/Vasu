document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    let firstName = document.getElementById("firstName").value;
    let lastName = document.getElementById("lastName").value;
    let gender = document.querySelector('input[name="gender"]:checked');
    let course = document.getElementById("course").value;
    let year = document.getElementById("year").value;
    let branch = document.getElementById("branch").value;
    let events = document.querySelectorAll('input[type="checkbox"]:checked');
    let performing = document.querySelector('input[name="perform"]:checked');
    let groupSize = document.getElementById("groupSize").value;
    if (!firstName || !lastName || !gender || !performing) {
        alert("Please fill in all required fields!");
        return;
    }
    if (performing.value === "Group" && (groupSize < 2 || groupSize > 5)) {
        alert("Group size must be between 2 and 5 members.");
        return;
    }
    let selectedEvents = [];
    events.forEach(event => selectedEvents.push(event.value));
    alert(`Thank you, ${firstName} ${lastName}! 
    You have registered for ${selectedEvents.join(", ")} in ${performing.value} category.`);
    
    this.reset(); 
});


