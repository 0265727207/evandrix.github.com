package org.gephi.desktop.neo4j;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.beans.PropertyChangeEvent;
import java.beans.PropertyChangeListener;
import java.io.File;
import javax.swing.AbstractAction;
import javax.swing.JFileChooser;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import org.gephi.desktop.neo4j.ui.DebugFileChooserComponent;
import org.gephi.desktop.neo4j.ui.DebugPanel;
import org.gephi.neo4j.api.Neo4jDelegateNodeDebugger;
import org.gephi.desktop.neo4j.ui.ExportOptionsPanel;
import org.gephi.desktop.neo4j.ui.TraversalFilterPanel;
import org.gephi.desktop.neo4j.ui.RemoteDatabasePanel;
import org.gephi.desktop.neo4j.ui.TraversalImportPanel;
import org.gephi.desktop.neo4j.ui.util.Neo4jUtils;
import org.gephi.neo4j.api.ClassNotFulfillRequirementsException;
import org.gephi.neo4j.api.FileSystemClassLoader;
import org.gephi.neo4j.api.MutableNeo4jDelegateNodeDebugger;
import org.gephi.neo4j.api.Neo4jExporter;
import org.gephi.neo4j.api.Neo4jImporter;
import org.gephi.neo4j.api.Neo4jVisualDebugger;
import org.gephi.project.api.ProjectController;
import org.gephi.project.api.Workspace;
import org.gephi.project.api.WorkspaceListener;
import org.gephi.utils.longtask.api.LongTaskExecutor;
import org.gephi.utils.longtask.spi.LongTask;
import org.gephi.visualization.VizController;
import org.neo4j.graphdb.GraphDatabaseService;
import org.netbeans.validation.api.ui.ValidationPanel;
import org.openide.DialogDescriptor;
import org.openide.DialogDisplayer;
import org.openide.NotifyDescriptor;
import org.openide.util.HelpCtx;
import org.openide.util.Lookup;
import org.openide.util.NbBundle;
import org.openide.util.actions.CallableSystemAction;


/**
 *
 * @author Martin Škurla
 */
public class Neo4jMenuAction extends CallableSystemAction {
    private JMenuItem localExport;
    private JMenuItem remoteExport;
    private JMenuItem debug;
    private JMenu menu;

    private boolean previousEdgeHasUniColor;


    public Neo4jMenuAction() {
        initializeMenu();

        Lookup.getDefault().lookup(ProjectController.class).addWorkspaceListener(new WorkspaceListener() {

            @Override
            public void initialize(Workspace workspace) {
                localExport .setEnabled(true);
                remoteExport.setEnabled(true);
                debug       .setEnabled(true);
            }

            @Override
            public void disable() {
                localExport .setEnabled(false);
                remoteExport.setEnabled(false);
                debug       .setEnabled(false);
            }

            @Override public void select(Workspace workspace) {}
            @Override public void unselect(Workspace workspace) {}
            @Override public void close(Workspace workspace) {}
        });
    }


    @Override
    public void performAction() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public String getName() {
        return "importNeo4jDB";
    }

    @Override
    public HelpCtx getHelpCtx() {
        return null;
    }

    @Override
    public JMenuItem getMenuPresenter() {
        return menu;
    }

    private void initializeMenu() {
        menu = new JMenu(NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_MenuLabel"));

        String localWholeImportMenuLabel = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_LocalWholeImportMenuLabel");
        JMenuItem localWholeImport = new JMenuItem(new AbstractAction(localWholeImportMenuLabel) {

            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                String localImportDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_LocalImportDialogTitle");
                fileChooser.setDialogTitle(localImportDialogTitle);

                Neo4jCustomDirectoryProvider.setEnabled(true);
                fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

                int dialogResult = fileChooser.showOpenDialog(null);

                Neo4jCustomDirectoryProvider.setEnabled(false);

                if (dialogResult == JFileChooser.CANCEL_OPTION)
                    return;

                final File neo4jDirectory = fileChooser.getSelectedFile();
                final GraphDatabaseService graphDB = Neo4jUtils.localDatabase(neo4jDirectory);

                String traversalDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_TraversalDialogTitle");
                final TraversalFilterPanel filterPanel = new TraversalFilterPanel();
                ValidationPanel validationPanel = filterPanel.createValidationPanel();

                if (validationPanel.showOkCancelDialog(traversalDialogTitle)) {
                    if (dialogResult == JFileChooser.APPROVE_OPTION) {
                        final Neo4jImporter neo4jImporter = Lookup.getDefault().lookup(Neo4jImporter.class);

                        LongTaskExecutor executor = new LongTaskExecutor(true);
                        executor.execute((LongTask) neo4jImporter, new Runnable() {

                            @Override
                            public void run() {
                                neo4jImporter.importDatabase(graphDB,
                                                             filterPanel.getFilterDescriptions(),
                                                             filterPanel.isRestrictModeEnabled(),
                                                             filterPanel.isMatchCaseEnabled());
                            }
                        });
                    }
                }
            }
        });

        String localTraversalImportMenuLabel = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_LocalTraversalImportMenuLabel");
        JMenuItem localTraversalImport = new JMenuItem(new AbstractAction(localTraversalImportMenuLabel) {

            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                String localImportDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_LocalImportDialogTitle");
                fileChooser.setDialogTitle(localImportDialogTitle);

                Neo4jCustomDirectoryProvider.setEnabled(true);
                fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

                int dialogResult = fileChooser.showOpenDialog(null);

                Neo4jCustomDirectoryProvider.setEnabled(false);

                if (dialogResult == JFileChooser.CANCEL_OPTION)
                    return;

                final File neo4jDirectory = fileChooser.getSelectedFile();
                final GraphDatabaseService graphDB = Neo4jUtils.localDatabase(neo4jDirectory);

                String traversalDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_TraversalDialogTitle");
                final TraversalImportPanel traversalPanel = new TraversalImportPanel(graphDB);
                ValidationPanel validationPanel = traversalPanel.createValidationPanel();

                if (validationPanel.showOkCancelDialog(traversalDialogTitle)) {
                    if (dialogResult == JFileChooser.APPROVE_OPTION) {
                        final Neo4jImporter neo4jImporter = Lookup.getDefault().lookup(Neo4jImporter.class);

                        LongTaskExecutor executor = new LongTaskExecutor(true);
                        executor.execute((LongTask) neo4jImporter, new Runnable() {

                            @Override
                            public void run() {
                                neo4jImporter.importDatabase(graphDB,
                                                             traversalPanel.getStartNodeId(),
                                                             traversalPanel.getOrder(),
                                                             traversalPanel.getMaxDepth(),
                                                             traversalPanel.getRelationshipDescriptions(),
                                                             traversalPanel.getFilterDescriptions(),
                                                             traversalPanel.isRestrictModeEnabled(),
                                                             traversalPanel.isMatchCaseEnabled());
                            }
                        });
                    }
                }
            }
        });

        String localExportMenuLabel = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_LocalExportMenuLabel");
        localExport = new JMenuItem(new AbstractAction(localExportMenuLabel) {
            public void actionPerformed(ActionEvent e) {
                String exportOptionsDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_ExportOptionsDialogTitle");
                final ExportOptionsPanel exportOptionsPanel= new ExportOptionsPanel();
                ValidationPanel validationPanel = exportOptionsPanel.createValidationPanel();
                validationPanel.showOkCancelDialog(exportOptionsDialogTitle);


                JFileChooser fileChooser = new JFileChooser();
                String localExportDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_LocalExportDialogTitle");
                fileChooser.setDialogTitle(localExportDialogTitle);

                fileChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

                int dialogResult = fileChooser.showOpenDialog(null);

                if (dialogResult == JFileChooser.APPROVE_OPTION) {
                    final File neo4jDirectory = fileChooser.getSelectedFile();
                    final Neo4jExporter neo4jExporter = Lookup.getDefault().lookup(Neo4jExporter.class);

                    LongTaskExecutor executor = new LongTaskExecutor(true);
                    executor.execute((LongTask) neo4jExporter, new Runnable() {
                        @Override
                        public void run() {
                            GraphDatabaseService graphDB = Neo4jUtils.localDatabase(neo4jDirectory);

                            neo4jExporter.exportDatabase(graphDB,
                                                         exportOptionsPanel.getFromColumn(),
                                                         exportOptionsPanel.getDefaultValue(),
                                                         exportOptionsPanel.getExportEdgeColumnNames(),
                                                         exportOptionsPanel.getExportNodeColumnNames());

                            graphDB.shutdown();
                        }
                    });
                }
            }
        });

        String remoteImportMenuLabel = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_RemoteImportMenuLabel");
        JMenuItem remoteImport = new JMenuItem(new AbstractAction(remoteImportMenuLabel) {
            public void actionPerformed(ActionEvent e) {
                final RemoteDatabasePanel databasePanel = new RemoteDatabasePanel();
                ValidationPanel validationPanel = databasePanel.createValidationPanel();
                String remoteImportDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_RemoteImportDialogTitle");

                if (validationPanel.showOkCancelDialog(remoteImportDialogTitle)) {
                    final Neo4jImporter neo4jImporter = Lookup.getDefault().lookup(Neo4jImporter.class);

                    LongTaskExecutor executor = new LongTaskExecutor(true);
                    executor.execute((LongTask) neo4jImporter, new Runnable() {
                        @Override
                        public void run() {
//TODO remoteImport dorobit...
//                            if (graphDB != null)
//                                graphDB.shutdown();
//
//                            graphDB = Neo4jUtils.remoteDatabase(databasePanel.getRemoteUrl(),
//                                                                databasePanel.getLogin(),
//                                                                databasePanel.getPassword());
//
//                            neo4jImporter.importDatabase(graphDB);
                        }
                    });
                }
            }
        });

        String remoteExportMenuLabel = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_RemoteExportMenuLabel");
        remoteExport = new JMenuItem(new AbstractAction(remoteExportMenuLabel) {
            public void actionPerformed(ActionEvent e) {
                final RemoteDatabasePanel databasePanel = new RemoteDatabasePanel();
                ValidationPanel validationPanel = databasePanel.createValidationPanel();
                String remoteExportDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_RemoteExportDialogTitle");

                if (validationPanel.showOkCancelDialog(remoteExportDialogTitle)) {
                    final Neo4jExporter neo4jExporter = Lookup.getDefault().lookup(Neo4jExporter.class);

                    LongTaskExecutor executor = new LongTaskExecutor(true);
                    executor.execute((LongTask) neo4jExporter, new Runnable() {
                        @Override
                        public void run() {
                            GraphDatabaseService graphDB = Neo4jUtils.remoteDatabase(databasePanel.getRemoteUrl(),
                                                                databasePanel.getLogin(),
                                                                databasePanel.getPassword());

                            neo4jExporter.exportDatabase(graphDB,//TODO >>> refactor like for local export with export dialog
                                                         null,
                                                         null,
                                                         null,
                                                         null);

                            graphDB.shutdown();
                        }
                    });
                }
            }
        });

        String debugMenuLabel = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_DebugMenuLabel");
        debug = new JMenuItem(new AbstractAction(debugMenuLabel) {

            public void actionPerformed(ActionEvent e) {
                JFileChooser fileChooser = new JFileChooser();
                String chooseDebugFileDialogTitle =
                        NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_ChooseDebugFileDialogTitle");
                fileChooser.setDialogTitle(chooseDebugFileDialogTitle);

                fileChooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
                fileChooser.setFileFilter(new Neo4jDebugFileFilter());
                fileChooser.setFileView(new Neo4jDebugFileView());
                fileChooser.setAccessory(new DebugFileChooserComponent(fileChooser));

                int dialogResult = fileChooser.showOpenDialog(null);

                if (dialogResult == JFileChooser.CANCEL_OPTION)
                    return;

                File neo4jDebugFile = fileChooser.getSelectedFile();
                FileSystemClassLoader classLoader =
                        Lookup.getDefault().lookup(FileSystemClassLoader.class);

                Class<?> loadedClass = null;

                try {
                    loadedClass = classLoader.loadClass(neo4jDebugFile,
                                                        enabled,
                                                        Neo4jDelegateNodeDebugger.class);
                }
                catch (ClassNotFoundException cnfe) {
                    showWarningMessage();
                    return;
                }
                catch (NoClassDefFoundError ncdfe) {
                    showWarningMessage();
                    return;
                }
                catch (ClassNotFulfillRequirementsException cnfre) {
                    showWarningMessage();
                    return;
                }
                catch (IllegalArgumentException iae) {
                    showWarningMessage();
                    return;
                }

                Neo4jDelegateNodeDebugger neo4jDebugger = null;
                try {
                    neo4jDebugger = (Neo4jDelegateNodeDebugger) loadedClass.newInstance();
                }
                catch (IllegalAccessException iae) {
                    throw new AssertionError();
                }
                catch (InstantiationException ie) {
                    throw new AssertionError();
                }

                // see GraphRestoration JavaDoc
                GraphRestoration graphRestoration = new GraphRestoration();

                previousEdgeHasUniColor =
                        VizController.getInstance().getVizModel().isEdgeHasUniColor();
                VizController.getInstance().getVizModel().setEdgeHasUniColor(true);

                String debugDialogTitle = NbBundle.getMessage(Neo4jMenuAction.class, "CTL_Neo4j_DebugOptionsDialogTitle");
                DialogDescriptor dialog = new DialogDescriptor(new DebugPanel(new MutableNeo4jDelegateNodeDebugger(neo4jDebugger)),
                                                               debugDialogTitle,
                                                               false,
                                                               graphRestoration);
                dialog.addPropertyChangeListener(graphRestoration);

                DialogDisplayer.getDefault().notify(dialog);
            }
        });


        menu.add(localWholeImport);
        menu.add(localTraversalImport);
        menu.add(remoteImport);
        menu.addSeparator();

        localExport.setEnabled(false);
        menu.add(localExport);
        remoteExport.setEnabled(false);
        menu.add(remoteExport);
        menu.addSeparator();

        debug.setEnabled(false);
        menu.add(debug);
    }

    private void showWarningMessage() {
        NotifyDescriptor notifyDescriptor =
                new NotifyDescriptor.Message("Selected file is not valid Neo4j debug file.",
                                             JOptionPane.WARNING_MESSAGE);

        DialogDisplayer.getDefault().notify(notifyDescriptor);
    }

    /*
     * This class is needed because of NetBeans platform. Action listener is used for
     * cases when user clicks OK/Cancel button. PropertyChangeListener is used for cases
     * when user clicks Cancel/Close button.
     *
     * We want to restore graph in all 3 cases, so we need to implement and register both
     * interfaces.
     */
    private class GraphRestoration implements PropertyChangeListener, ActionListener {
        private final Neo4jVisualDebugger neo4jVisualDebugger =
                Lookup.getDefault().lookup(Neo4jVisualDebugger.class);


        @Override
        public void propertyChange(PropertyChangeEvent evt) {
            neo4jVisualDebugger.restore();
            VizController.getInstance().getVizModel().setEdgeHasUniColor(previousEdgeHasUniColor);
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            neo4jVisualDebugger.restore();
            VizController.getInstance().getVizModel().setEdgeHasUniColor(previousEdgeHasUniColor);
        }
    }
}
