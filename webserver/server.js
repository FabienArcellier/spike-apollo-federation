const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require('@apollo/gateway');
const {  } = require('@apollo/gateway')

const gateway = new ApolloGateway({
    serviceList: [
      { name: 'accounts', url: 'http://localhost:8000' },
    ],
    debug : true
});
  
const server = new ApolloServer({ gateway, subscriptions: false, });
//server.listen();