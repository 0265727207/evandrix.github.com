/*
Copyright 2008 WebAtlas
Authors : Mathieu Bastian, Mathieu Jacomy, Julian Bilcke
Website : http://www.gephi.org

This file is part of Gephi.

Gephi is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gephi is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Gephi.  If not, see <http://www.gnu.org/licenses/>.
 */
package org.gephi.branding.desktop.reporter;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import org.openide.DialogDescriptor;
import org.openide.DialogDisplayer;
import org.openide.util.NbBundle;
import org.w3c.dom.Document;

/**
 *
 * @author Mathieu Bastian
 */
public class ReportPanel extends javax.swing.JPanel {

    private Report report;
    private ReportController reportController;

    public ReportPanel(Report report) {
        this.report = report;
        initComponents();

        //Bind
        followCheckBox.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                labelEmail.setEnabled(followCheckBox.isSelected());
                emailTextField.setEnabled(followCheckBox.isSelected());
                helpLabel.setEnabled(followCheckBox.isSelected());
            }
        });
        labelEmail.setEnabled(followCheckBox.isSelected());
        emailTextField.setEnabled(followCheckBox.isSelected());
        helpLabel.setEnabled(followCheckBox.isSelected());
        viewDataButton.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent e) {
                //Set
                ReportPanel.this.report.setUserDescription(problemArea.getText());
                ReportPanel.this.report.setUserEmail(emailTextField.getText());
                Document document = reportController.buildReportDocument(ReportPanel.this.report);
                DialogDescriptor dd = new DialogDescriptor(new ViewDataPanel(document), NbBundle.getMessage(ReportPanel.class, "ReportPanel.viewData.title"), true, DialogDescriptor.DEFAULT_OPTION, null, null);
                DialogDisplayer.getDefault().notify(dd);
            }
        });

        setup();
    }

    private void setup() {
        summaryTextField.setText(report.getSummary());
        emailTextField.setText(report.getUserEmail());
        problemArea.setText(report.getUserDescription());
    }

    public void showDialog() {
        reportController = new ReportController();
        Object[] options = new Object[2];
        options[0] = NbBundle.getMessage(ReportPanel.class, "ReportPanel.dialog.sendButton");
        options[1] = DialogDescriptor.CANCEL_OPTION;
        String title = NbBundle.getMessage(ReportPanel.class, "ReportPanel.dialog.title");

        DialogDescriptor dd = new DialogDescriptor(this, title, true, options, options[0], DialogDescriptor.DEFAULT_ALIGN, null, null);
        if (DialogDisplayer.getDefault().notify(dd) == options[0]) {
            //Set
            report.setUserDescription(problemArea.getText());
            report.setUserEmail(emailTextField.getText());
            reportController.sendReport(report);
        }
    }

    /** This method is called from within the constructor to
     * initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is
     * always regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        summaryTextField = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        problemArea = new javax.swing.JTextArea();
        jLabel2 = new javax.swing.JLabel();
        followCheckBox = new javax.swing.JCheckBox();
        labelEmail = new javax.swing.JLabel();
        emailTextField = new javax.swing.JTextField();
        helpLabel = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        viewDataButton = new javax.swing.JButton();

        jLabel1.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.jLabel1.text")); // NOI18N

        summaryTextField.setEditable(false);
        summaryTextField.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.summaryTextField.text")); // NOI18N

        problemArea.setColumns(20);
        problemArea.setRows(5);
        jScrollPane1.setViewportView(problemArea);

        jLabel2.setFont(new java.awt.Font("Tahoma", 1, 11));
        jLabel2.setForeground(new java.awt.Color(0, 73, 204));
        jLabel2.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.jLabel2.text")); // NOI18N

        followCheckBox.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.followCheckBox.text")); // NOI18N

        labelEmail.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.labelEmail.text")); // NOI18N

        emailTextField.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.emailTextField.text")); // NOI18N

        helpLabel.setFont(new java.awt.Font("Tahoma", 0, 10));
        helpLabel.setForeground(new java.awt.Color(102, 102, 102));
        helpLabel.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.helpLabel.text")); // NOI18N

        jLabel3.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.jLabel3.text")); // NOI18N

        viewDataButton.setText(org.openide.util.NbBundle.getMessage(ReportPanel.class, "ReportPanel.viewDataButton.text")); // NOI18N

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(this);
        this.setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel3)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 128, Short.MAX_VALUE)
                        .addComponent(viewDataButton))
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 572, Short.MAX_VALUE)
                    .addComponent(jLabel2, javax.swing.GroupLayout.DEFAULT_SIZE, 572, Short.MAX_VALUE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(jLabel1)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(summaryTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 520, Short.MAX_VALUE))
                    .addComponent(followCheckBox)
                    .addGroup(layout.createSequentialGroup()
                        .addGap(21, 21, 21)
                        .addComponent(labelEmail)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(helpLabel, javax.swing.GroupLayout.DEFAULT_SIZE, 517, Short.MAX_VALUE)
                            .addComponent(emailTextField, javax.swing.GroupLayout.DEFAULT_SIZE, 517, Short.MAX_VALUE))))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 14, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(viewDataButton))
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                            .addComponent(jLabel1)
                            .addComponent(summaryTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(jLabel2)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, 149, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(218, 218, 218)
                        .addComponent(followCheckBox)))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(emailTextField, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(labelEmail))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(helpLabel)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
    }// </editor-fold>//GEN-END:initComponents
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JTextField emailTextField;
    private javax.swing.JCheckBox followCheckBox;
    private javax.swing.JLabel helpLabel;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel labelEmail;
    private javax.swing.JTextArea problemArea;
    private javax.swing.JTextField summaryTextField;
    private javax.swing.JButton viewDataButton;
    // End of variables declaration//GEN-END:variables
}
