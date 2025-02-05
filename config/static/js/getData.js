
let infoList = [];
let logsList = [];

const listInfo = () => {
  $.ajax({
    url: "/info/info",
    type: "GET",
    contentType: "application/json",
    async: true,
    success: (info) => {
      info.sort((a, b) => b.idreg - a.idreg);
      infoList = info;
    },
    error: (error) => {
      console.error(error);
    },
  });
};

const listLogs = () => {
    $.ajax({
        url: "/logs/logs",
        type: "GET",
        contentType: "application/json",
        async: true,
        success: (info) => {
        info.sort((a, b) => b.idreg - a.idreg);
        logsList = info;
        },
        error: (error) => {
        console.error(error);
        },
    });
};

listInfo();
listLogs();