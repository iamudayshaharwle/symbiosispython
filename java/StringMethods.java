class StringMethods {
    public static void main(String[] args) {
        String name = "Figthher";
        int val = name.length();
        System.out.println(val);
        String lower = name.toLowerCase();
        System.out.println(lower);
        System.out.println(name.toUpperCase());
        System.out.println(name.trim());
        System.out.println(name.substring(2,5));
        System.out.println(name.replace("g","mm"));
        System.out.println(name.startsWith("Fi"));
        System.out.println(name.endsWith("er"));
        System.out.println(name.charAt(5));
        System.out.println(name.indexOf("h",2));
        System.out.println(name.lastIndexOf("h",6));
        System.out.println(name.equals("Figthher"));
        System.out.println(name.equalsIgnoreCase("figthher"));
        System.out.println("\t\t*\n\t*\t*\t*\n*\t*\t*\t*\t*\n\t*\t*\t*\n\t\t*");
    


 
    }
}