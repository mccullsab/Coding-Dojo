const Author = require('../models/authors.models.js')

const controller = {
    testRoute: (req, res) => {
        res.send("Our express api server is now sending this over to the browser");
    },

    getAll: (req, res) => {
        Author.find()
            .then((allAuthors) => {
                res.json({ author: allAuthors });
            })
            .catch((err) =>
                res.status(500).json({ message: "whoops - something is not working", error: err })
            );
    },

    create: (req, res) => {
        Author.create(req.body)
            .then((newlyCreatedAuthor) => {
                res.json({ author: newlyCreatedAuthor });
            })
            .catch((err) =>
                res.status(500).json({ message: "whoops - something is not working", error: err })
            );
    },

    getOne: (req, res) => {
        Author.findOne({ _id: req.params.id })
            .then((oneAuthor) => {
                res.json({ author: oneAuthor });
            })
            .catch((err) =>
                res.status(500).json({ message: "whoops - something is not working", error: err })
            );
    },

    update: (req, res) => {
        Author.findOneAndUpdate({ _id: req.params.id }, req.body, { 
            new: true,
            runValidators: true
        })
            .then((updatedAuthor) => {
                res.json({ author: updatedAuthor });
            })
            .catch((err) =>
                res.status(500).json({ message: "whoops - something is not working", error: err })
            );
    },

    delete: (req, res) => {
        Author.deleteOne({ _id: req.params.id })
            .then((result) => {
                res.json({ result });
            })
            .catch((err) =>
                res.status(500).json({ message: "whoops - something is not working", error: err })
            );
    }
}

module.exports = controller