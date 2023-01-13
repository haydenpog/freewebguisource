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
        float reach = 0;
        bool reachtog = false;

       

        private void button1_Click(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString(yoursite + "getcfg/" + username);
            char yes = char.Parse("|");
            string[] features = webData.Split(yes);
            // AUTOCLICK
            if (features[0].Contains("True"))
            {
                leftbind = (int)(char.Parse(features[0].Substring(features[0].Length - 1))) - 32;
                label3.Text = features[0].Substring(features[0].Length - 1);
                features[0] = features[0].Remove(features[0].Length - 1);
                label1.Text = "True";
                autotog = true;
                features[0] = features[0].Replace("True", "");
                cps = Int32.Parse(features[0]);
                label2.Text = cps.ToString();
            }
            else if (features[0].Contains("None"))
            {
                leftbind = (int)(char.Parse(features[0].Substring(features[0].Length - 1))) - 32;
                features[0] = features[0].Remove(features[0].Length - 1);
                label1.Text = "Off";
                autotog = false;
                features[0] = features[0].Replace("None", "");
                cps = Int32.Parse(features[0]);
                label2.Text = cps.ToString();

            }

            // REACH
            if (features[1].Contains("True"))
            {
                label5.Text = "True";
                reachtog = true;
                features[1] = features[1].Replace("True", "");
                reach = float.Parse(features[1]);
                label4.Text = reach.ToString();
            }
            else if (features[1].Contains("None"))
            {
                label5.Text = "Off";
                reachtog = false;
                features[1] = features[1].Replace("None", "");
                reach = float.Parse(features[1]);
                label4.Text = reach.ToString();

            }
        }

        private void Form2_Load(object sender, EventArgs e)
        {


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString(yoursite + "getcfg/" + username);
            char yes = char.Parse("|");
            string[] features = webData.Split(yes);
            // AUTOCLICK
            if (features[0].Contains("True"))
            {
                leftbind = (int)(char.Parse(features[0].Substring(features[0].Length - 1))) - 32;
                label3.Text = features[0].Substring(features[0].Length - 1);
                features[0] = features[0].Remove(features[0].Length - 1);
                label1.Text = "True";
                autotog = true;
                features[0] = features[0].Replace("True", "");
                cps = Int32.Parse(features[0]);
                label2.Text = cps.ToString();
            }
            else if (features[0].Contains("None"))
            {
                leftbind = (int)(char.Parse(features[0].Substring(features[0].Length - 1))) - 32;
                features[0] = features[0].Remove(features[0].Length - 1);
                label1.Text = "Off";
                autotog = false;
                features[0] = features[0].Replace("None", "");
                cps = Int32.Parse(features[0]);
                label2.Text = cps.ToString();

            }
            
            // REACH
            if (features[1].Contains("True"))
            {
                label5.Text = "True";
                reachtog = true;
                features[1] = features[1].Replace("True", "");
                reach = float.Parse(features[1]);
                label4.Text = reach.ToString();
            }
            else if (features[1].Contains("None"))
            {
                label5.Text = "Off";
                reachtog = false;
                features[1] = features[1].Replace("None", "");
                reach = float.Parse(features[1]);
                label4.Text = reach.ToString();

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();
            string webData = wc.DownloadString(yoursite + "getcfg/" + username);
            char yes = char.Parse("|");
            string[] features = webData.Split(yes);
            if (features[0].Contains("True"))
            {
                wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("None"));
                // only issue with this aproach is that people can edit other peoples configs if they know their name. Most people who dont know this source wont figure this out but its still good 4 u to know.
           
            }
            else if (features[0].Contains("None"))
            {
                wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("True"));
                // only issue with this aproach is that people can edit other peoples configs if they know their name. Most people who dont know this source wont figure this out but its still good 4 u to know.

            }
        }

        public bool clikced = false;
        private void button3_Click(object sender, EventArgs e) { }


        private void button3_KeyDown_1(object sender, KeyEventArgs e)
        {
           
        }

        private void timer2_Tick(object sender, EventArgs e)
        {

            if (WinApi.GetAsyncKeyState(leftbind) != 0) 
            {
                Thread.Sleep(500);
                
                System.Net.WebClient wc = new System.Net.WebClient();
                string webData = wc.DownloadString(yoursite + "getcfg/" + username);
                char yes = char.Parse("|");
                string[] features = webData.Split(yes);
                if (features[0].Contains("True"))
                {
                    wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("None"));
                    // only issue with this aproach is that people can edit other peoples configs if they know their name. Most people who dont know this source wont figure this out but its still good 4 u to know.

                }
                else if (features[0].Contains("None"))
                {
                    wc.UploadData(yoursite + "set/" + username, Encoding.ASCII.GetBytes("True"));
                    // only issue with this aproach is that people can edit other peoples configs if they know their name. Most people who dont know this source wont figure this out but its still good 4 u to know.

                }
            }
        }

        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {
            // SELF DESTRUCT
        }
    }
}
