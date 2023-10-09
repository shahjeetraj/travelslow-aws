document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  // Use Compose form post to point to sendEmail function
  document.querySelector("#compose-form").addEventListener("submit",sendEmail);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#single-email-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#single-email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  // fetch all emails for the respective mailbox folder like inbox, sent or archive
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print Log for the email data
    console.log(emails);
    const mailBox = document.createElement('div');
    mailBox.classList.add('container');
  
    document.getElementById('emails-view').appendChild(mailBox);
    const mailHeaders = document.createElement('div');
      mailHeaders.classList.add('row');
      mailHeaders.style.border = "thin solid grey";
      mailHeaders.style.marginBottom = "2px";
      mailHeaders.style.padding = "3px";

    if (mailbox == 'sent') {
      mailHeaders.innerHTML = `
        <div class="col">Recipients</div>
        <div class="col">Subject</div>
        <div class="col">Date</div>`;
    } else {
      mailHeaders.innerHTML = `
        <div class="col">Sender</div>
        <div class="col">Subject</div>
        <div class="col">Date</div>`;
    }
    
    mailBox.appendChild(mailHeaders);
    
    if (emails.length == 0) {
      const mailNotFound = document.createElement('div');
      mailNotFound.classList.add('row');
      mailNotFound.style.border = "thin solid grey";
      mailNotFound.style.marginBottom = "2px";
      mailNotFound.style.padding = "3px";
      mailNotFound.innerHTML = `
        <div class="col text-center">Hooray! No Emails Here!!</div>
        `;
      
      mailBox.appendChild(mailNotFound);
    } else {
      // Display emails by going thru entire array returned from above service and showing in a card
    emails.forEach(individual_mail => {
      // Creating an html view for every email

    const mailItem = document.createElement('div');
    mailItem.classList.add('row');
    mailItem.style.border = "thin solid grey";
    mailItem.style.padding = "3px";
    mailItem.style.marginBottom = "2px";
    if (individual_mail.read == true) {
      mailItem.style.backgroundColor = "#dedede";
    } else {
      mailItem.style.backgroundColor = "white";
    }
    
    const recipientsDiv = document.createElement('div');
      recipientsDiv.classList.add('col');

    individual_mail.recipients.forEach(recipient => {
      recipientsDiv.innerHTML = `
        ${recipient}
      `;
    });
    const senderCol = document.createElement('div');
    senderCol.classList.add('col');
    senderCol.innerHTML = `
    ${individual_mail.sender}
    `;
    
    const subjectCol = document.createElement('div');
    subjectCol.classList.add('col');
    subjectCol.innerHTML = `
    ${individual_mail.subject}
    `;

    const datetimeDiv = document.createElement('div');
    datetimeDiv.classList.add('col');
    datetimeDiv.innerHTML = `
      ${individual_mail.timestamp}
    `;
    
    if (mailbox == 'sent') {
      mailBox.appendChild(mailItem);
      mailItem.appendChild(recipientsDiv);
      mailItem.appendChild(subjectCol);
      mailItem.appendChild(datetimeDiv);
    } else {
      mailBox.appendChild(mailItem);
      mailItem.appendChild(senderCol);
      mailItem.appendChild(subjectCol);
      mailItem.appendChild(datetimeDiv);
    }
  
    // Append the mailItem to the document where you need it.
    
      mailItem.addEventListener('click', function() {
        viewEmail(individual_mail.id);
      });
      
            
    });
    }

});
  


    // ... do something else with emails ...
}

function viewEmail(id){
  console.log(id);

  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {
      // Print email
      console.log(email);
      // Change mail read status to read when mail is opened if unread.
      if (email.read == false) {
        fetch(`/emails/${email.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
      }
      
      // Show Single Email view and hide other views
      document.querySelector('#emails-view').style.display = 'none';
      document.querySelector('#compose-view').style.display = 'none';
      document.querySelector('#single-email-view').style.display = 'block';
      const d1 = new Date(email.timestamp); 
      const d2 = new Date(); 
        
      const diff = d2.getTime() - d1.getTime(); 
        
      const daydiff = Math.floor(diff / (1000 * 60 * 60 * 24));
      let dayDays = '';
      if (daydiff == 1) {
        dayDays = '1 day ago';
      } else if (daydiff == 0) {
        dayDays = 'today!';
      } else {
        dayDays = daydiff+' days ago';
      }

      document.getElementById('single-email-view').innerHTML = `
      <div class="card text-start">
      <div class="card-header">
      <div class="row">
      <div class="col">
        Sender: ${email.sender}
      </div>
      <div class="col">
        Recipients: ${email.recipients}
      </div>
      <div class="col"><strong>Subject: ${email.subject}</strong></div>
      </div>
      </div>
      <div class="card-body">
        <h5 class="card-title"></h5>
        
        <p class="card-text text-start">${email.body}</p>
        <div class="btn-toolbar" role="toolbar">
          <div class="btn-group me-2" role="group" style="margin-right: 4px">
            <button type="button" id="btnArch"></button>
          </div>
          <div class="btn-group me-2" role="group" style="margin-right: 4px">
            <button type="button" id="btnReadUnread"</button>
          </div>
          <div class="btn-group me-3" role="group" style="margin-right: 4px">
            <button type="button" id="btnReply"</button>
          </div>
        </div>
      </div>
      <div class="card-footer text-muted">
      Date of Email: ${email.timestamp}. That was ${dayDays} 
      </div>
      </div>
     
      `
      // Handling Archive and UnArchive button and logic
      document.getElementById("btnArch").innerHTML = email.archived ? "Un-Archive" : "Archive";
      document.getElementById("btnArch").className = email.archived ? "btn btn-sm btn-outline-warning" : "btn btn-sm btn-outline-success";
      btnArch.addEventListener('click', function () {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              archived: !email.archived
          })
        })
        .then(() => {load_mailbox('archive')})

      });

      // Handling Read and UnRead button and logic
      document.getElementById("btnReadUnread").innerHTML = email.read ? "Mark Unread" : "Mark Read";
      document.getElementById("btnReadUnread").className = email.read ? "btn btn-sm btn-outline-primary" : "btn btn-sm btn-outline-secondary";
      btnReadUnread.addEventListener('click', function () {
        fetch(`/emails/${email.id}`, {
          method: 'PUT',
          body: JSON.stringify({
              read: !email.read
          })
        })
        .then(() => {load_mailbox('inbox')})

      });

      // Handling Replybutton and logic
      document.getElementById("btnReply").innerHTML = "Reply";
      document.getElementById("btnReply").className = "btn btn-sm btn-outline-info";
      btnReply.addEventListener('click', function () {
        compose_email();
        // Prefill composition fields
        document.querySelector('#compose-recipients').value = email.sender;
        let subject = email.subject;
        if (subject.split(' ',1)[0] != "Re:") {
          subject = "Re: " + email.subject;
        }
        document.querySelector('#compose-subject').value = subject;
        document.querySelector('#compose-body').value = `\n---------------------------------------------------\nOn ${email.timestamp} ${email.sender} wrote: \n` + email.body;

      });

  });

}

  // Create sendEmail Function
  function sendEmail(event) {
    event.preventDefault(); //to stop submitting page and going to inbox.
    const mailReceiver = document.getElementById("compose-recipients").value;
    const mailSubject = document.getElementById("compose-subject").value;
    const mailBody = document.getElementById("compose-body").value;
    
    // use above variables and post them to compose view
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: mailReceiver,
          subject: mailSubject,
          body: mailBody
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
        load_mailbox('sent')
    });
  }