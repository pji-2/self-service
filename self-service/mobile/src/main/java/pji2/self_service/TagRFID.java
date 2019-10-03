package pji2.self_service;

public class TagRFID {
    private byte idTag[];

    public TagRFID() {
        this.idTag = null;
    }

    public boolean lerTag(){
        return false;
    }

    public byte[] getIdTag() {
        return idTag;
    }
}
