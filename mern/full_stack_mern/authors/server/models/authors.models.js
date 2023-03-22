const mongoose = require('mongoose');

const AuthorScheuma = new mongoose.Schema({
    name: {
        type: String,
        required: [true, "name required"],
        minlength: [3, "must be at least 3 characters"]
    }
}, { timestamps: true });

const Author = mongoose.model('Author', AuthorScheuma);

module.exports = Author;