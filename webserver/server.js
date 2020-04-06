const { ApolloServer } = require('apollo-server');
const { ApolloGateway } = require('@apollo/gateway');
const {  } = require('@apollo/gateway')

const gateway = new ApolloGateway({
    serviceList: [
      { name: 'accounts', url: 'http://localhost:8000' },
      { name: 'accounts2', url: 'http://localhost:8001' },
    ],
    debug : true
});
  
const server = new ApolloServer({ gateway, subscriptions: false, });
server.listen();