package project202020;

import java.awt.Image;
import java.awt.PopupMenu;
import java.awt.Robot;
import java.awt.SystemTray;
import java.awt.Toolkit;
import java.awt.TrayIcon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class TrayNotification {

    static PopupMenu exitMenu = new PopupMenu("exit");
    static Image image = Toolkit.getDefaultToolkit().getImage("eye.png");
    static TrayIcon trayIcon = new TrayIcon(image, "20/20/20", exitMenu);

    public static void main(String[] a) throws Exception {
        if (SystemTray.isSupported()) {
            SystemTray tray = SystemTray.getSystemTray();

            trayIcon.setImageAutoSize(true);
            tray.add(trayIcon);
            trayIcon.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    try {
                        ProcessBuilder pb = new ProcessBuilder("C:\\Program Files\\nircmd\\nircmd.exe", "monitor", "off");
                        Process p = pb.start();
                        Thread.sleep(500);
                        p.destroyForcibly();
                        Thread.sleep(20000);
                        Robot robot = new Robot();
                        robot.mouseMove(500, 500);

                    } catch (Exception e1) {
                        e1.printStackTrace();
                    }
                }
            });
            new Thread(){
                public void run() {
                    while (true){
                        trayIcon.displayMessage("Eye break!", "It's been 20 min! Double click on the Eye-con to take a 20 sec break. :)", TrayIcon.MessageType.INFO);
                        try {
                            sleep(1200000);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            }.start();
        }
    }

}
