const AuthorController = require('../controllers/authors.controllers')

const routes = (app) => {
    app.get("/api", AuthorController.testRoute);
    app.get("/api/authors", AuthorController.getAll);
    app.post("/api/authors", AuthorController.create);
    app.get("/api/authors/:id", AuthorController.getOne);    
    app.put("/api/authors/:id", AuthorController.update);
    app.delete("/api/authors/:id", AuthorController.delete);
};

module.exports = routes