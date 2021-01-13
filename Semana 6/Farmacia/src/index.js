const Server = require('./config/Server');
const miServidor = new Server();
miServidor.start();

// cmd
// heroku logs --tail --app nombre_app
