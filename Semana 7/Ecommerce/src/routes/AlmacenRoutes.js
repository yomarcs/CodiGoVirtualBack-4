const { Router } = require("express");
const almacen_controller = require("../controllers/AlmacenController");
const almacen_router = Router();

almacen_router.post('/almacen', almacen_controller.createAlmacen);

module.exports = almacen_router;