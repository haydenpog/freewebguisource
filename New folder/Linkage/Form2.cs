using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System;
using System.Drawing;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace Linkage
{
    public partial class Form2 : Form
    {
        string username;
        public Form2(string s)
        {
            InitializeComponent();
            username = s;
        }
        string yoursite = "http://127.0.0.1:5000/";
        bool autotog = false;
        int cps = 0;
        int leftbind = 0;

       

        private void button1_Click(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString(yoursite + "getcfg/" + username);
            if (webData.Contains("True"))
            {
                label3.Text = webData.Substring(webData.Length - 1);
                leftbind = (int)(char.Parse(webData.Substring(webData.Length - 1))) - 32;
                webData = webData.Remove(webData.Length - 1);
                label1.Text = "True";
                autotog = true;
                webData = webData.Replace("True", "");
                cps = Int32.Parse(webData);
                label2.Text = cps.ToString();
            }
            else if (webData.Contains("None"))
            {
                leftbind = (int)(char.Parse(webData.Substring(webData.Length - 1))) - 32;
                webData = webData.Remove(webData.Length - 1);
                label1.Text = "Off";
                autotog = false;
                webData = webData.Replace("None", "");
                cps = Int32.Parse(webData);
                label2.Text = cps.ToString();
            }
        }

        private void Form2_Load(object sender, EventArgs e)
        {


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString(yoursite + "getcfg/" + username);
            if (webData.Contains("True"))
            {
                leftbind = (int)(char.Parse(webData.Substring(webData.Length - 1))) - 32;
                label3.Text = webData.Substring(webData.Length - 1);
                webData = webData.Remove(webData.Length - 1);
                label1.Text = "True";
                autotog = true;
                webData = webData.Replace("True", "");
                cps = Int32.Parse(webData);
                label2.Text = cps.ToString();
            }
            else if (webData.Contains("None"))
            {
                leftbind = (int)(char.Parse(webData.Substring(webData.Length - 1))) - 32;
                webData = webData.Remove(webData.Length - 1);
                label1.Text = "Off";
                autotog = false;
                webData = webData.Replace("None", "");
                cps = Int32.Parse(webData);
                label2.Text = cps.ToString();

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString(yoursite + "getcfg/" + username);
            if (webData.Contains("True"))
            {
               // wc.UploadString(yoursite + "set/" + username, "None");
                wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("None"));
                
            }
            else if (webData.Contains("None"))
            {
                wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("True"));

               // wc.UploadString(yoursite + "set/" + username, "True");
            }
        }

        public bool clikced = false;
        private void button3_Click(object sender, EventArgs e) { clikced = true; button3.Text = "[...]"; }


        private void button3_KeyDown_1(object sender, KeyEventArgs e)
        {
            if (clikced == true)
            {
                switch (e.KeyCode)
                {
                    case Keys.Escape:
                        leftbind = 0;
                        button3.Text = "[N/A]";
                        clikced = false;
                        break;

                    default: 
                        leftbind = (int)e.KeyCode;
                        button3.Text = "[" + e.KeyCode + "]";
                        MessageBox.Show(leftbind.ToString());
                        clikced = false;
                        break; 
                }
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {

            if (WinApi.GetAsyncKeyState(leftbind) != 0) 
            {
                Thread.Sleep(500);
                
                System.Net.WebClient wc = new System.Net.WebClient();
                string webData = wc.DownloadString(yoursite + "getcfg/" + username);
                if (webData.Contains("True"))
                {
                    wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("None"));

                }
                else if (webData.Contains("None"))
                {
                    wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("True"));
                }
            }
        }

        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {
            // SELF DESTRUCT
        }
    }
}
