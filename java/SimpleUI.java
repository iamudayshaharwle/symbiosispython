import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleUI extends JFrame {
    private JTextField textField;
    private JButton button;
    private JLabel label;

    public SimpleUI() {
        setTitle("Simple UI");
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setSize(300, 150);
        setLocationRelativeTo(null);

        textField = new JTextField(10);
        button = new JButton("Click Me!");
        label = new JLabel("Enter your name:");

        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String name = textField.getText();
                JOptionPane.showMessageDialog(null, "Hello, " + name + "!");
            }
        });

        setLayout(new FlowLayout());
        add(label);
        add(textField);
        add(button);

        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new SimpleUI();
            }
        });
    }
}
