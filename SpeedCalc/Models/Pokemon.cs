using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace SpeedCalc.Models
{
    public class Pokemon : Mon
    {
        public Mon mon;

        public Natures nature;
        public Types type1;
        public Types type2;
        public Stats EVs;
        public Stats IVs;
        public Stats Modifiers;

    }
}
