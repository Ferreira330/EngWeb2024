var mongoose = require('mongoose')
var passportLocalMongoose = require('passport-local-mongoose')

var userSchema = new  mongoose.Schema({
    username: String,
    password: String,
    name: String,
    email: String,
    filiacao: String,
    nivel: String,
    dataRegisto: String,
    dataUltimoAcesso: String
})

userSchema.plugin(passportLocalMongoose)

module.exports = mongoose.model('user', userSchema)