require('dotenv').config();

const express = require("express");
const app = express();
const port = process.env.PORT;

require('./config/mongoose.config');

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const routes = require("./routes/jokes.routes");
routes(app);

const server = app.listen(port, () =>
    console.log(`Server is locked and loaded on port ${server.address().port}!`)
);