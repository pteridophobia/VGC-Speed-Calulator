using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public class Mon
    {
        public int ID;
        public int dexNum;
        public string name;
        public Stats baseStats;
        public Types type1;
        public Types type2;

        public Mon(int dex, string pname, Stats bs, Types t1, Types t2)
        {
            // This constructor will take info from serebii.net, create an object, and store the object information in database
            this.ID = dex;
            this.dexNum = dex;
            this.name = pname;
            this.baseStats = bs;
            this.type1 = t1;
            this.type2 = t2;
            //TODO: insert data into a database if not already present
        }

        public Mon(int dex)
        {
            // This will be called if the database is already full
            // TODO: find the mon in database with dexNum == dex amd set values
        }

    }
}
