using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Windows.Forms;
using static Ascii85;
namespace Linkage
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        string yoursite = "http://127.0.0.1:5000/";
        string decode(string str)
        {
            Ascii85 a = new Ascii85();
            byte[] decoded = a.Decode(str);
            str = Encoding.ASCII.GetString(decoded);
            byte[] yay = Base32ToBytes(str);
            str = Encoding.ASCII.GetString(yay);
            string lastCharacter = str.Substring(str.Length - 1);
            string secondtolastCharacter = str.Substring(str.Length - 2);
            secondtolastCharacter.Replace(lastCharacter, "");
            str = str.Replace(lastCharacter, secondtolastCharacter);
            str = str.Replace(secondtolastCharacter + lastCharacter, "");
            var valueBytes = System.Convert.FromBase64String(str + "==");
            str = Encoding.UTF8.GetString(valueBytes);
            return str;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            System.Net.WebClient wc = new System.Net.WebClient();

            string webData2 = wc.DownloadString(yoursite + "db/" + textBox1.Text + "/" + textBox2.Text + "/" + DateTime.UtcNow.ToString("yyyy-MM-dd"));
            if (webData2.Contains("1"))
                {
                Form2 fm2 = new Form2(textBox1.Text);
                fm2.Show();
                this.Hide();

            }
        }

        public static byte[] Base32ToBytes(string base32)
        {
            const string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
            List<byte> output = new List<byte>();
            char[] bytes = base32.ToCharArray();
            for (int bitIndex = 0; bitIndex < base32.Length * 5; bitIndex += 8)
            {
                int dualbyte = alphabet.IndexOf(bytes[bitIndex / 5]) << 10;
                if (bitIndex / 5 + 1 < bytes.Length)
                    dualbyte |= alphabet.IndexOf(bytes[bitIndex / 5 + 1]) << 5;
                if (bitIndex / 5 + 2 < bytes.Length)
                    dualbyte |= alphabet.IndexOf(bytes[bitIndex / 5 + 2]);

                dualbyte = 0xff & (dualbyte >> (15 - bitIndex % 5 - 8));
                output.Add((byte)(dualbyte));
            }
            return output.ToArray();
        }

        

       

        private void Form1_Load(object sender, EventArgs e)
        {
            //int yes = (int)(char.Parse("q"));
            //MessageBox.Show(yes.ToString());
        }
    }
}
