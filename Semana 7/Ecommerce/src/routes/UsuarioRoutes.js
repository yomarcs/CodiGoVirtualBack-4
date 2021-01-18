const { Router } = require("express");
const usuario_controller = require("../controllers/UsuarioController");
const { wachiman } = require("../utils/Validador");
const usuario_router = Router();

usuario_router.post("/registrar", usuario_controller.registrarUsuario);
usuario_router.post("/login", usuario_controller.login);
usuario_router.get("/usuario", wachiman, usuario_controller.devolverUsuarioPorToken);

module.exports = usuario_router;
