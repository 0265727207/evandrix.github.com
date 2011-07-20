package org.gephi.neo4j.impl;


import org.gephi.data.attributes.api.AttributeColumn;
import org.gephi.data.attributes.spi.AttributeValueDelegateProvider;
import org.gephi.data.attributes.spi.GraphItemDelegateFactoryProvider;
import org.gephi.data.attributes.type.AbstractList;
import org.gephi.data.properties.PropertiesColumn;
import org.neo4j.graphdb.DynamicRelationshipType;
import org.neo4j.graphdb.GraphDatabaseService;


class Neo4jDelegateProviderImpl extends AttributeValueDelegateProvider<Long> {
    private static final Neo4jDelegateProviderImpl instance;

    
    static {
        instance = new Neo4jDelegateProviderImpl();
    }

    public static Neo4jDelegateProviderImpl getInstance() {
        return instance;
    }

    private Neo4jDelegateProviderImpl() {}


    @Override
    public String storageEngineName() {
        return "Neo4j";
    }

    @Override
    public Object getNodeAttributeValue(Long delegateId, AttributeColumn attributeColumn) {
        GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

        return graphDB.getNodeById(delegateId).getProperty(attributeColumn.getId());
    }

    @Override
    public void setNodeAttributeValue(Long delegateId, AttributeColumn attributeColumn, Object nodeValue) {
        // will work for both adding new and overriding previous value
        if (nodeValue instanceof AbstractList)
            nodeValue = ListTypeToPrimitiveArrayConvertor.convert(nodeValue);

        GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();
        
        graphDB.getNodeById(delegateId).setProperty(attributeColumn.getId(), nodeValue);
    }

    @Override
    public void deleteNodeAttributeValue(Long delegateId, AttributeColumn attributeColumn) {
        GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

        graphDB.getNodeById(delegateId).removeProperty(attributeColumn.getId());
    }


    @Override
    public Object getEdgeAttributeValue(Long delegateId, AttributeColumn attributeColumn) {
        GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

        if (attributeColumn.getId().equals(PropertiesColumn.NEO4J_RELATIONSHIP_TYPE.getId()))
            return graphDB.getRelationshipById(delegateId).getType().name();
        else
            return graphDB.getRelationshipById(delegateId).getProperty(attributeColumn.getId());
    }

    @Override
    public void setEdgeAttributeValue(Long delegateId, AttributeColumn attributeColumn, Object edgeValue) {
        // will work for both adding new and overriding previous value
        if (edgeValue instanceof AbstractList)
            edgeValue = ListTypeToPrimitiveArrayConvertor.convert(edgeValue);

        GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

        graphDB.getRelationshipById(delegateId).setProperty(attributeColumn.getId(), edgeValue);
    }

    @Override
    public void deleteEdgeAttributeValue(Long delegateId, AttributeColumn attributeColumn) {
        GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

        graphDB.getRelationshipById(delegateId).removeProperty(attributeColumn.getId());
    }

    public GraphItemDelegateFactoryProvider<Long> graphItemDelegateFactoryProvider() {
        return Neo4jGraphItemDelegateFactoryProviderImpl.getInstance();
    }

    private static class ListTypeToPrimitiveArrayConvertor {
        private ListTypeToPrimitiveArrayConvertor() {}

        static Object convert(Object listTypeObject) {
            return null;//TODO >>> finish conversion
        }
    }

    private static class Neo4jGraphItemDelegateFactoryProviderImpl implements GraphItemDelegateFactoryProvider<Long> {
        private static final Neo4jGraphItemDelegateFactoryProviderImpl instance;
        private static final String DEFAULT_RELATIONSHIP_TYPE_NAME = "";


        static {
            instance = new Neo4jGraphItemDelegateFactoryProviderImpl();
        }

        public static Neo4jGraphItemDelegateFactoryProviderImpl getInstance() {
            return instance;
        }
        

        @Override
        public Long createNode() {
            GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

            return graphDB.createNode().getId();
        }

        @Override
        public void deleteNode(Long nodeId) {
            GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

            graphDB.getNodeById(nodeId).delete();
        }

        @Override
        public Long createEdge(Long startNodeId, Long endNodeId) {
            GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

            org.neo4j.graphdb.Node startNode = graphDB.getNodeById(startNodeId);
            org.neo4j.graphdb.Node endNode   = graphDB.getNodeById(endNodeId);

            return startNode.createRelationshipTo(endNode,
                                                  DynamicRelationshipType.withName(DEFAULT_RELATIONSHIP_TYPE_NAME)).getId();
        }

        @Override
        public void deleteEdge(Long edgeId) {
            GraphDatabaseService graphDB = GraphModelImportConverter.getGraphDBForCurrentWorkspace();

            graphDB.getRelationshipById(edgeId).delete();
        }
    }
}
