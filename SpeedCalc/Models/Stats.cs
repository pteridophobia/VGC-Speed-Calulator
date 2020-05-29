using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public class Stats
    {
        public int HP;
        public int Attack;
        public int Defense;
        public int SpAttack;
        public int SpDefense;
        public int Speed;

        public Stats copmuteStatValues(Stats bse, Stats evs, Stats ivs, Stats mods/*TOADD: board state*/)
        {
            //TODO: implement calculations of stats
            return bse;
        }
    }

}
